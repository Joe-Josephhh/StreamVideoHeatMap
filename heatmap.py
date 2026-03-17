import numpy as np
import cv2

heatmap = None

def update_heatmap(frame, tracks):
    global heatmap

    h, w = frame.shape[:2]

    if heatmap is None:
        heatmap = np.zeros((h, w), dtype=np.float32)

    for track in tracks:
        if not track.is_confirmed():
            continue

        l, t, r, b = map(int, track.to_ltrb())
        cx, cy = (l+r)//2, (t+b)//2

        heatmap[cy, cx] += 1

    return heatmap


def overlay_heatmap(frame, heatmap):
    heatmap_norm = cv2.normalize(heatmap, None, 0, 255, cv2.NORM_MINMAX)
    heatmap_color = cv2.applyColorMap(heatmap_norm.astype('uint8'), cv2.COLORMAP_JET)

    return cv2.addWeighted(frame, 0.7, heatmap_color, 0.3, 0)