from typing import *
from pathlib import Path
from src.word_reading.word_recognition import WordRecognition
from src.word_reading.word_sampler import WordSampler
from src.utils.utils import save_json


class WordCAPTCHA:
    def __init__(
        self,
        path: Union[str, Path] = "./gui/static/assets/words.json",
        num_words: int = 5,
        unique: bool = True,
        calibration_time: int = 1,
        verbose: bool = True,
        threshold: float = 0.5,
        log: str = "./gui/static/logs/word_reading.json",
        web: bool = True,
    ):
        """Initialize test.

        Args:
            path (Union[str, Path], optional): JSON file path. Defaults to "./gui/static/assets/words.json".
            num_words (int, optional): Number of words to be sampled. Defaults to 5.
            unique (bool, optional): If true we sample words uniquely. Defaults to True.
            calibration_time (int, optional): Time needed to calibrate the microphone to noise ambient. Defaults to 1.
            verbose (bool, optional): If true prints some informations. Defaults to True.
            threshold (float, optional): Threshold to pass for the test to be true. Defaults to 0.5.
            log (str, optional): File in which we log some informations, used to communicate with the frontend. Defaults to "./word_reading.json".
            web (bool, optional): If true we run the model on a web GUI. Defaults to True.
        """
        self.verbose = verbose
        self.threshold = threshold
        self.log_path = log
        self.web = web

        # * Word sampling.
        self.ws = WordSampler(path=path)
        self.n = num_words
        self.unique = unique

        # * Word recognition.
        self.wr = WordRecognition(
            calibration_time=calibration_time, verbose=self.verbose
        )

        # * Output.
        self.out = {"human": [], "machine": []}
        # Logging.
        self.log_data = {"truth": [], "preds": [], "passed": 0}

    def sample(self):
        """Sample words and save them to a JSON file."""
        words_gt = self.ws.sample(self.n, unique=self.unique)
        if self.verbose:
            print("Sampled words: ", words_gt)

        # * Save json file.
        self.log_data["truth"] = words_gt
        save_json(path=self.log_path, data=self.log_data)

    def listen(self):
        words = self.wr(verbose=self.verbose)
        if self.verbose:
            print("Recognized words: ", words)
        # Save log.
        self.log_data["preds"] = words
        save_json(path=self.log_path, data=self.log_data)

    def run(self) -> Dict:
        """Run the CAPTCHA test.

        Returns:
            Dict: Machine generated correct outputs and human guesses.
        """
        # * Word sampling.
        words_gt = self.ws.sample(self.n, unique=self.unique)
        print("EDO", words_gt)
        if self.verbose:
            print("Sampled words: ", words_gt)

        # * Recognition.
        words = self.wr(verbose=self.verbose)
        if self.verbose:
            print("Recognized words: ", words)
        self.out = {"human": words, "machine": words_gt}
        return self.out

    def eval(self) -> Optional[bool]:
        """Evaluate if the user passed the test and how.

        Returns:
            Optional[bool]: True if the test has been passed.
        """
        assert (
            self.out or self.log_data
        ), "Before evaluation you need to run the handler."

        if self.web:
            words_h = set(self.log_data["preds"])
            words_m = set(self.log_data["truth"])
        else:
            words_h = set(self.out["human"])
            words_m = set(self.out["machine"])

        # Count occurrences.
        cnt = 0
        for h in words_h:
            if h in words_m:
                cnt += 1

        test = cnt / len(words_m) >= self.threshold

        if self.web and test:
            self.log_data["passed"] = int(test)
            save_json(path=self.log_path, data=self.log_data)
        else:
            return test
