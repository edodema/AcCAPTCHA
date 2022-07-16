from typing import *
from pathlib import Path
from src.speech.word_recognition import WordRecognition
from src.utils.word_sampler import WordSampler


class Handler:
    def __init__(
        self,
        path: Union[str, Path] = "./assets/words.json",
        num_words: int = 5,
        unique: bool = True,
        calibration_time: int = 1,
        verbose: bool = True,
        threshold: float = 0.5,
    ):
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
        words_gt = self.ws.sample(self.n, unique=self.unique)
        if self.verbose:
            print("Sampled words: ", words_gt)

        words = self.wr(verbose=self.verbose)
        if self.verbose:
            print("Recognized words: ", words)
        self.out = {"human": words, "machine": words_gt}
        return self.out

    def eval(self) -> bool:
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
    handler = Handler(calibration_time=10)
    handler.run()
    test = handler.eval()
    print(test)
