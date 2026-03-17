from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

model = YOLO("yolov8n.pt")
tracker = DeepSort(max_age=30)

def detect_and_track(frame):
    results = model(frame)
    detections = []

    for r in results:
        for box in r.boxes:
            if int(box.cls[0]) == 0:  # person
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                w, h = x2 - x1, y2 - y1
                detections.append(([x1, y1, w, h], 1.0, 'person'))

    tracks = tracker.update_tracks(detections, frame=frame)

    count = 0
    tracked_ids = []

    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        l, t, w, h = map(int, track.to_ltrb())
        
        tracked_ids.append(track_id)
        count += 1

        # Draw ID
        import cv2
        cv2.rectangle(frame, (l,t), (l+w,t+h), (0,255,0), 2)
        cv2.putText(frame, f"ID {track_id}", (l,t-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)

    return frame, count, tracked_ids