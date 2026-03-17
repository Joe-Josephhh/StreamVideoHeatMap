import cv2
from camera import init_camera, get_frame
from detection import detect_and_track
from storage import save_data
from heatmap import update_heatmap, overlay_heatmap

cap = init_camera()

while True:
    frame = get_frame(cap)
    if frame is None:
        break

    frame, count, tracks = detect_and_track(frame)

    heatmap = update_heatmap(frame, tracks)
    frame = overlay_heatmap(frame, heatmap)

    save_data(count)

    cv2.putText(frame, f"Count: {count}", (20,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("Analytics", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()