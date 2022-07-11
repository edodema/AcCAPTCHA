from typing import *
from pathlib import Path
import numpy as np
import cv2 as cv

if __name__ == "__main__":
    HOME_PATH = Path(".")
    ASSETS_PATH = HOME_PATH / "assets"
    IMG_PATH = ASSETS_PATH / "five_hand.jpg"

    img = cv.imread(IMG_PATH.as_posix())
    cv.imshow("Image", img)
