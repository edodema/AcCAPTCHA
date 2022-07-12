from typing import *
import cv2 as cv
import numpy as np

# TODO: Add as a parameter a function or class, we will use that function for any of them.
# TODO: Add window resolution.
# TODO: Fix for different modalities.


class VideoCapture:
    def __init__(self, quit_key: str = "q"):
        """Initialize object.

        Args:
            quit_key (str, optional): Key that interrupts video capture when pressed. Defaults to "q".
        """
        self.vid = cv.VideoCapture(0)
        self.esc = quit_key

    def __call__(self, mod: Any, mirror: bool = True):
        while True:
            # Capture the video frame by frame.
            ret, frame = self.vid.read()

            # Call modality on image.
            mod(frame)

            # Mirror image.
            if mirror:
                frame = cv.flip(src=frame, flipCode=1)
            # Display the resulting frame
            cv.imshow("", frame)

            # Quitting button.
            if cv.waitKey(1) & 0xFF == ord(self.esc):
                break

        # Release the capture object.
        self.vid.release()
        # Destroy all the windows
        cv.destroyAllWindows()
