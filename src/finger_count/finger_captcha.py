from typing import *
import random
import cv2 as cv
import numpy as np

from src.finger_count.finger_count import FingerCount
from src.finger_count.video_capture import VideoCapture
from src.utils.utils import save_json


class FingerCAPTCHA:
    def __init__(
        self,
        width_roi: float = 0.3,
        height_roi: float = 0.5,
        size_kpts: int = 5,
        color_kpts: tuple = (255, 255, 0),
        thickness_kpts: int = -1,
        line_hand: int = -1,
        rgb_cvt: bool = False,
        draw_kpts: bool = True,
        display_count: bool = False,
        threshold: int = 0.2,
        n_fingers: int = 5,
        color_roi: tuple = (255, 0, 0),
        thickness_roi: int = 3,
        log: str = "./gui/static/logs/finger_count.json",
        acceptance_threhsold: int = 50,
    ):
        """Initialize CAPTCHA test.

        Args:
            width_roi (float, optional): Width of the ROI rectangle. Defaults to 0.3.
            height_roi (float, optional): Height of the ROI rectangle. Defaults to 0.5.
            size_kpts (int, optional): Size of the shown keypoints' circle. Defaults to 5.
            color_kpts (tuple, optional): Color of the shown keypoints' circle. Defaults to (255, 255, 0).
            thickness_kpts (int, optional): Thickness of the shown keypoints' circle. Defaults to -1.
            line_hand (int, optional): Type of line in the hand skeleton. Defaults to -1.
            rgb_cvt (bool, optional): Flag for RGB conversion. Defaults to False.
            draw_kpts (bool, optional): Flag for drawing keypoints. Defaults to True.
            display_count (bool, optional): Flag for displaying finger count. Defaults to False.
            threshold (int, optional): Tolerance threshold for our results. Defaults to 0.2.
            n_fingers (int, optional): Number of fingers in one hand. Defaults to 5.
            color_roi (tuple, optional): Color of the ROI rectangle. Defaults to (255, 0, 0).
            thickness_roi (int, optional): Thickness of the ROI rectangle. Defaults to 3.
            log (str, optional): File in which we log some informations, used to communicate with the frontend. Defaults to "./logs/finge_count.json".
            acceptance_threshold (int, optional): Minimum number of correct guesses needed to consider the test passed. Defaults to 100.
        """
        self.width = width_roi
        self.height = height_roi
        self.threshold = threshold
        self.n_fingers = n_fingers
        self.color_roi = color_roi
        self.thickness_roi = thickness_roi
        self.log_path = log
        self.acceptance_threshold = acceptance_threhsold

        # * Finger counting.
        self.fc = FingerCount(
            size=size_kpts,
            color=color_kpts,
            thickness=thickness_kpts,
            line=line_hand,
            rgb=rgb_cvt,
            draw=draw_kpts,
            display=display_count,
        )

        # * A flag to sample ROI's corners.
        self.corners = True
        self.target = self.sample_number(n_fingers=self.n_fingers)

        # * Dictionary used to store log data.
        self.log_data = {"target": self.target, "passed": 0, "preds": []}
        # Save JSON, since we need to print the number.
        save_json(path=self.log_path, data=self.log_data)

        # * Accumulators to get the correct counts.
        self.counts = []

    def run(self, src: np.ndarray) -> Dict:
        """Run the test.

        Args:
            src (np.ndarray): Input image.

        Returns:
            Dict: Output dictionary consisting of the original image, chosen and predicted number.
        """
        img = self.draw_roi(src)
        roi = img[self.y : self.v, self.x : self.u]

        count = self.fc(roi)

        if count > -1:
            self.counts.append(count)
            # Add estimated count to the log.
            self.log_data["preds"] += [count]

        # * Save file when we reach a threshold.
        # Filter numbers, saving only ones that match the target.
        filtered = list(
            filter(lambda pred: pred == self.target, self.log_data["preds"])
        )
        if len(filtered) >= self.acceptance_threshold:
            self.log_data["passed"] = 1
            save_json(path=self.log_path, data=self.log_data)
        else:
            # TODO: Remove
            print(False, len(filtered), count, self.target)

        return {"img": img, "count": count, "truth": self.target}

    def sample_number(self, n_fingers: int = 5) -> int:
        """Sample a number that should be shown to the camera.

        Args:
            n_fingers (int, optional): Number of fingers in an hand, we will pick at maximum this number. Defaults to 5.

        Returns:
            int: Picker number.
        """
        return random.randint(0, n_fingers - 1)

    def sample_corners(self, src: np.ndarray) -> Tuple[int, int, int, int]:
        """Pick a random ROI in the image, we define it using the top-left and bottom-right vertices.

        Args:
            src (np.ndarray): Input image.

        Returns:
            Tuple[int, int, int, int]: (x, y, u, v) i.e., top-left (x, y) and bottom right (u, v).
        """
        h, w, _ = src.shape

        # Define the sides of the ROI.
        h_roi = int(self.height * h)
        w_roi = int(self.width * w)

        # Sample top-left corner.
        y = random.randint(0, h - h_roi - 1)
        x = random.randint(0, w - w_roi - 1)

        # Compute bottom-right corner.
        v = y + h_roi
        u = x + w_roi

        # No need to sample further point.
        self.corners = False

        return (x, y, u, v)

    def draw_roi(self, src: np.ndarray) -> np.ndarray:
        """Draw a ROI on the image.

        Args:
            src (np.ndarray): Input image.

        Returns:
            np.ndarray: Output image.
        """
        # If needed get the top-left corner.
        if self.corners:
            self.x, self.y, self.u, self.v = self.sample_corners(src)

        img = cv.rectangle(
            src,
            (self.x, self.y),
            (self.u, self.v),
            color=self.color_roi,
            thickness=self.thickness_roi,
        )
        return img
