from typing import *
import cv2 as cv
import numpy as np

# TODO: Add as a parameter a function or class, we will use that function for any of them.
# TODO: Add window resolution.
# TODO: Fix for different modalities.


class VideoCapture:
    def __init__(self, web: bool = False, quit_key: str = "q"):
        """Initialize object.

        Args:
            web (bool, optional): Use video capture in a web browser. Defaults to False.
            quit_key (str, optional): Key that interrupts video capture when pressed. Defaults to "q".
        """
        self.vid = cv.VideoCapture(0)
        self.web = web
        self.esc = quit_key

    def __call__(self, mod: Any, mirror: bool = True):
        if self.web:
            # * Online.
            while True:
                _, frame = self.vid.read()

                # * Process image.
                frame = self.process(frame, mod, mirror)

                # * Return byte encoded image.
                _, jpg = cv.imencode(".jpg", frame)
                jpg_b = jpg.tobytes()

                yield (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" + jpg_b + b"\r\n\r\n"
                )
        else:
            # * Offline
            while True:
                # Capture the video frame by frame.
                _, frame = self.vid.read()

                # * Process image.
                frame = self.process(frame, mod, mirror)

                # Display the resulting frame
                cv.imshow("", frame)

                # Quitting button.
                if cv.waitKey(1) & 0xFF == ord(self.esc):
                    break

            # Release the capture object.
            self.vid.release()
            # Destroy all the windows
            cv.destroyAllWindows()
            return None

    def process(self, frame: np.ndarray, mod: Any, mirror: bool) -> np.ndarray:
        # Call modality on image.
        out = mod(frame)

        truth = out["truth"]
        count = out["count"]

        # TODO: remove
        # print(truth, count)

        # Mirror image.
        if mirror:
            frame = cv.flip(src=frame, flipCode=1)

        print(type(frame))
        return frame
