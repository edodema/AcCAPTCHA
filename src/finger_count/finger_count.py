#
# * Reference: https://www.section.io/engineering-education/creating-a-finger-counter/

from typing import *
from pathlib import Path

import cv2 as cv
import mediapipe as mp
import numpy as np


class FingerCount:
    def __init__(
        self,
        size: int = 5,
        color: tuple = (255, 255, 0),
        thickness: int = -1,
        line: int = -1,
        rgb: bool = False,
        draw: bool = False,
        display: bool = False,
    ):
        """Initialization.

        Args:
            size (int, optional): Picture's keypoints size. Defaults to 5.
            color (tuple, optional): Picture's keypoints color. Defaults to (255, 255, 0).
            thickness (int, optional): Picture's keypoints thickness. Defaults to 1.
            line (int, optional): Picture's line type. Defaults to -1.
            rgb (bool, optional): Convert image to rgb. Defaults to False.
            draw (bool, optional): Draw hand skeleton. Defaults to False.
            display (bool, optional): Print on video the count number, if draw is true numbers will be mirrored as well. Defaults to False.
        """
        # MediaPipe object.
        self.hands = mp.solutions.hands.Hands()
        # Finger coordinates.
        self.thumb = (4, 2)
        self.fingers = [(8, 6), (12, 10), (16, 14), (20, 18)]

        self.rgb = rgb
        # Drawing options.
        self.size = size
        self.color = color
        self.thickness = thickness
        self.line = line
        self.draw = draw
        self.display = display

    def __call__(self, src: np.ndarray) -> int:
        """Apply finger counting.

        Args:
            src (np.ndarray): Source image.

        Returns:
            int: The number of fingers counted.
        """
        # Convert imgage to RGB.
        if self.rgb:
            img = cv.cvtColor(src, cv.COLOR_BGR2RGB)
        else:
            img = src

        # Extract landmark points.
        result = self.hands.process(img)
        landmarks = result.multi_hand_landmarks

        # Get keypoints.
        keypoints = self.get_keypoints(src, landmarks)

        # Count fingers.
        if keypoints:
            cnt = self.count_fingers(src, keypoints)
        else:
            cnt = -1

        return cnt

    def get_keypoints(self, img: np.ndarray, landmarks: list) -> list:
        """Get keypoints.

        Args:
            img (np.ndarray): Source image.
            landmarks (list): Landmark points.

        Returns:
            list: Keypoints.
        """
        keypoints = []
        if landmarks:
            for landmark in landmarks:
                # Draw connections.
                if self.draw:
                    mp.solutions.drawing_utils.draw_landmarks(
                        img, landmark, mp.solutions.hands.HAND_CONNECTIONS
                    )
                for lm in landmark.landmark:
                    # Convert hand point coordinates to image pixels.
                    h, w, _ = img.shape
                    x, y = int(lm.x * w), int(lm.y * h)
                    keypoints.append((x, y))

        # Draw keypoints.
        if self.draw:
            for point in keypoints:
                cv.circle(
                    img,
                    center=point,
                    radius=self.size,
                    color=self.color,
                    thickness=self.thickness,
                    lineType=self.line,
                )
        return keypoints

    def count_fingers(self, img: np.ndarray, keypoints: list) -> int:
        """Count open fingers. The thumb is open when over the palm, other fingers when over the phalanx.

        Args:
            img (np.ndarray): Source image.
            keypoints (list): Keypoints.

        Returns:
            int: Number of fingers.
        """
        # Checking whether a finger is open or closed
        cnt = 0

        # Thumb.
        if keypoints[self.thumb[0]][0] > keypoints[self.thumb[1]][0]:
            cnt += 1
        # Other fingers.
        for coordinate in self.fingers:
            if keypoints[coordinate[0]][1] < keypoints[coordinate[1]][1]:
                cnt += 1

        # ! For debug purposes only.
        if self.display:
            cv.putText(
                img, str(cnt), (150, 150), cv.FONT_HERSHEY_PLAIN, 12, (0, 255, 0), 12
            )

        return cnt
