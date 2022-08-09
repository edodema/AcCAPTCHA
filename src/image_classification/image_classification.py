from operator import index
from typing import *
from pathlib import Path
import json
import random
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

from src.utils.utils import save_json


class ImageCAPTCHA:
    def __init__(
        self,
        path: Union[str, Path] = "./gui/static/assets/images/index.json",
        log: str = "./gui/static/logs/image_classification.json",
        num_choices: int = 4,
    ):
        self.path = Path(".") / path
        self.data = self._load_data()
        self.log_path = log

        # * Sample an image and save it.
        img_path, self.tgt = self.sample()

        # Sample false class.
        choices = self.get_random_options(num_choices)

        # Save dictionary.
        # ! Here "static/" is hardcoded, it should not be an issue.
        self.log_data = {
            "truth": self.tgt,
            "path": "static/" + img_path,
            "choices": choices,
        }
        save_json(path=self.log_path, data=self.log_data)

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

    def get_random_options(self, num_choices: int) -> List:
        """Sample three random classes as the wrong answers.

        Args:
            num_choices (int): Number of wrong answers.

        Returns:
            List: Output list of classes.
        """
        classes = set(self.data.values())

        # Remove the gold truth, we do not want repetitions.
        classes.remove(self.tgt)
        # Add it to the out choices.
        choices = [self.tgt]

        # Sample elements, we do not allow repetitions.
        for _ in range(num_choices - 1):
            choice = random.choice(list(classes))
            choices.append(choice)
            classes.remove(choice)

        # Shuffle, to avoid having the first answer as always correct.
        random.shuffle(choices)
        return choices

    def show(self, path: Union[str, Path]):
        """Show an image.
        # TODO Not really needed, debug purposes only.

        Args:
            path (Union[str, Path]): Image path.
        """
        img = mpimg.imread(path)
        plt.imshow(img)
        plt.show()

    def read_input(self) -> str:
        """Read user input.
        # TODO Not really needed, debug purposes only.

        Returns:
            str: User input.
        """
        return input("Enter your value: ")


if __name__ == "__main__":
    tc = ImageCAPTCHA()
    # path, object = tc.sample()
    # tc.show(path)
    # tc.read_input()
