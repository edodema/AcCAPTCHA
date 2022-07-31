from typing import *
import cv2 as cv
import numpy as np


class VideoCapture:
    def __init__(self, quit_key: str = "q"):
        """Initialize object.

        Args:
            quit_key (str, optional): Key that interrupts video capture when pressed. Defaults to "q".
        """
        self.vid = cv.VideoCapture(0)
        self.esc = quit_key

    def __call__(self, f: Any, mirror: bool = True):
        """Run video capture.

        Args:
            f (Any): Function to apply to frames.
            mirror (bool, optional): If true mirror image. Defaults to True.

        Yields:
            Generator[bytes]: _description_
        """
        while True:
            _, frame = self.vid.read()

            # * Process image.
            frame = self.process(frame, f, mirror)

            # * Return byte encoded image.
            _, jpg = cv.imencode(".jpg", frame)
            jpg_b = jpg.tobytes()

            yield (
                b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + jpg_b + b"\r\n\r\n"
            )

    def process(self, frame: np.ndarray, f: Any, mirror: bool) -> np.ndarray:
        """Process frame.

        Args:
            frame (np.ndarray): Input frame.
            mod (Any): Function to apply to frame.
            mirror (bool): Mirror video.

        Returns:
            np.ndarray: Processed frame.
        """
        # Call modality on image.
        out = f(frame)

        truth = out["truth"]
        count = out["count"]

        # TODO: remove
        # print(truth, count)

        # Mirror image.
        if mirror:
            frame = cv.flip(src=frame, flipCode=1)

        print(type(frame))
        return frame
