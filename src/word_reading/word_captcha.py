from typing import *
from pathlib import Path
from src.word_reading.word_recognition import WordRecognition
from src.word_reading.word_sampler import WordSampler


class WordCAPTCHA:
    def __init__(
        self,
        path: Union[str, Path] = "./gui/static/assets/words.json",
        num_words: int = 5,
        unique: bool = True,
        calibration_time: int = 1,
        verbose: bool = True,
        threshold: float = 0.5,
    ):
        """Initialize test.

        Args:
            path (Union[str, Path], optional): JSON file path. Defaults to "./gui/static/assets/words.json".
            num_words (int, optional): Number of words to be sampled. Defaults to 5.
            unique (bool, optional): If true we sample words uniquely. Defaults to True.
            calibration_time (int, optional): Time needed to calibrate the microphone to noise ambient. Defaults to 1.
            verbose (bool, optional): If true prints some informations. Defaults to True.
            threshold (float, optional): Threshold to pass for the test to be true. Defaults to 0.5.
        """
        self.verbose = verbose
        self.threshold = threshold

        # * Word sampling.
        self.ws = WordSampler(path=path)
        self.n = num_words
        self.unique = unique

        # * Word recognition.
        self.wr = WordRecognition(
            calibration_time=calibration_time, verbose=self.verbose
        )

    def run(self) -> Dict:
        """Run the CAPTCHA test.

        Returns:
            Dict: Machine generated correct outputs and human guesses.
        """
        words_gt = self.ws.sample(self.n, unique=self.unique)
        if self.verbose:
            print("Sampled words: ", words_gt)

        words = self.wr(verbose=self.verbose)
        if self.verbose:
            print("Recognized words: ", words)
        self.out = {"human": words, "machine": words_gt}
        return self.out

    def eval(self) -> bool:
        """Evaluate if the user passed the test and how.

        Returns:
            bool: True if the test has been passed.
        """
        assert self.out, "Before evaluation you need to run the handler."

        words_h = set(self.out["human"])
        words_m = set(self.out["machine"])

        # Count occurrences.
        cnt = 0
        for h in words_h:
            if h in words_m:
                cnt += 1

        test = cnt / len(words_m) >= self.threshold
        return test


if __name__ == "__main__":
    captcha = WordCAPTCHA()
    captcha.run()
    captcha.eval()
