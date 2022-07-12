from typing import *
import cv2 as cv

from src.utils.video_capture import VideoCapture
from src.gesture.finger_count import FingerCount

if __name__ == "__main__":
    vc = VideoCapture()
    fc = FingerCount(draw=True, display=True)

    vc(mod=fc)
