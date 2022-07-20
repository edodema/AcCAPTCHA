from operator import index
from typing import *
from pathlib import Path
import json
import random
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class ImageClassification:
    def __init__(self, path: Union[str, Path] = "./assets/images/index.json"):
        self.path = Path(".") / path
        self.data = self._load_data()

    def _load_data(self) -> Dict:
        """Load the dataset as a dictionary.

        Returns:
            Dict: Dataset.
        """
        with open(self.path, "r") as f:
            data = json.load(f)
        return data

    def sample(self) -> Tuple[str, str]:
        """Sample a random text.

        Returns:
            Tuple[str, str]: Text and image path.
        """
        return random.choice(list(self.data.items()))

    def show(self, path: Union[str, Path]):
        """Show an image.
        # ! Not really needed, debug purposes only.

        Args:
            path (Union[str, Path]): Image path.
        """
        img = mpimg.imread(path)
        plt.imshow(img)
        plt.show()

    def read_input(self) -> str:
        """Read user input.

        Returns:
            str: User input.
        """
        return input("Enter your value: ")


if __name__ == "__main__":
    tc = ImageClassification()
    path, object = tc.sample()
    print(object)
    tc.show(path)
    tc.read_input()
