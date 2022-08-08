from typing import *
import json
import random
from pathlib import Path


class WordSampler:
    def __init__(self, path: Union[str, Path] = "./gui/static/assets/words.json"):
        """Initialize object.

        Args:
            path (Union[str, Path], optional): Path of the corpus file. Defaults to "./gui/static/assets/words.json".
        """
        self.corpus = self.load_json(path)
        self.max = len(self.corpus) - 1

    def sample(self, n: int, unique: bool = False) -> list:
        """Randomly sample words from the text corpus.

        Args:
            n (int): Number of words we want to sample.
            unique (bool, optional): It true the words will all be unique. Defaults to False.

        Returns:
            list: List of sampled words.
        """
        if unique:
            samples = set()
            while len(samples) < n:
                samples.add(self.corpus[str(random.randint(0, self.max))])
            samples = list(samples)
        else:
            samples = [
                self.corpus[str(random.randint(0, self.max))] for _ in range(0, n)
            ]

        return samples

    def load_json(self, path: Union[str, Path]) -> Dict:
        """Load a JSON file in a dictionary object.

        Args:
            path (Union[str, Path]): Path of the JSON file.

        Returns:
            Dict: JSON word dictinary.
        """
        f = open(path)
        file = json.load(f)
        f.close()
        return file

    def save_json(self, obj: dict, path: Union[str, Path]):
        """Save a JSON.

        Args:
            obj (dict): Dictionary we want to save.
            path (Union[str, Path]): Path where to save the file.
        """
        f = open(path, "w")
        json.dump(obj, f, indent=-1)
        f.close()


# if __name__ == "__main__":
#     HOME = Path(".")
#     ASSET = HOME / "assets"
#     JSON_FILE = ASSET / "words.json"

#     ws = WordSampler(JSON_FILE)
#     samples = ws.sample(10, unique=False)
#     print(samples)
