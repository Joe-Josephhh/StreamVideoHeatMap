import cv2

def init_camera():
    return cv2.VideoCapture("http://192.168.1.6:4747/video")

def get_frame(cap):
    ret, frame = cap.read()
    return frame if ret else None