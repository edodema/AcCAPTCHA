from typing import *
import json


def save_json(path: str, data: Dict):
    """Save a dictionary as a JSON file.

    Args:
            path (str): Path where the file will be saved.
            data (Dict): Log data as a dictionary.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=-1)
