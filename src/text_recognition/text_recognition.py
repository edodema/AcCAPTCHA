from typing import *
from pathlib import Path
import json
import random
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from src.utils.utils import save_json

# Remove unnecessary attributes


class TextCAPTCHA:
    def __init__(
        self,
        path: Union[str, Path] = "./gui/static/assets/captcha/index.json",
        log_path: str = "./gui/static/logs/text_recognition.json",
    ):
        self.path = Path(".") / path
        self.data = self._load_data()

        # * Sample a fragment and save it.
        self.tgt, text_path = self.sample()

        # Save dictionary.
        # ! Here "static/" is hardcoded, it should not be an issue.
        self.log_data = {
            "truth": self.tgt,
            "path": "static/" + text_path,
        }
        save_json(path=log_path, data=self.log_data)

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
        # TODO: Remove

        Args:
            path (Union[str, Path]): Image path.
        """
        img = mpimg.imread(path)
        plt.imshow(img)
        plt.show()

    def read_input(self) -> str:
        """Read user input.
        # TODO Remove

        Returns:
            str: User input.
        """
        return input("Enter your value: ")
