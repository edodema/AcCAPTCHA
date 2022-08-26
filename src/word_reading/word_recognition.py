from typing import *
import speech_recognition as sr


class WordRecognition:
    def __init__(self, calibration_time: int = 1, verbose: bool = True):
        """Initialize object.

        Args:
            calibration_time (int, optional): Time spent calibrating on ambient noise. Defaults to 1.
            verbose (bool, optional): If true print some information. Defaults to True.
        """
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        # Calibrating microphone device to ambient noise.
        if verbose:
            print("Calibrating...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=calibration_time)
        print(
            "Minimum energy threshold: {:.3f}".format(self.recognizer.energy_threshold)
        )

    def __call__(self, verbose: bool = True) -> List[str]:
        """Apply word recognition.

        Args:
            verbose (bool, optional): I true print some information. Defaults to True.

        Returns:
            List[str]: List of recognized words.
        """
        audio = self.listen(verbose=verbose)
        words = self.recognize(audio, verbose=verbose)
        return words

    def listen(self, verbose: bool = True) -> sr.AudioData:
        """Listen to the microphone.

        Args:
            verbose (bool, optional): If true print some information. Defaults to True.

        Returns:
            sr.AudioData: Perceived audio input.
        """
        if verbose:
            print("Say something...")
        with self.microphone as source:
            audio = self.recognizer.listen(source=source)
        return audio

    def recognize(self, audio: sr.AudioData, verbose: bool = True) -> List[str]:
        """Recognize what said.

        Args:
            audio (sr.AudioData): Audio data obtained through SpeechRecognition.
            verbose (bool, optional): If true print some informations. Defaults to True.

        Returns:
            List[str]: A list of recognized words.
        """
        if verbose:
            print("Recognizing...")
        words = self.google(audio)
        return words

    def google(self, audio: sr.AudioData) -> List[str]:
        """Recognize spoken words using the Google API.

        Args:
            audio (sr.AudioData): Audio data obtained through SpeechRecognition.
            verbose (bool, optional): If true print some information. Defaults to True.

        Returns:
            List[str]: A list of recognized words.
        """
        try:
            text = self.recognizer.recognize_google(audio)
            # Handle data to correctly print unicode characters to standard output.
            words = text.split(" ")
            return words
        except sr.UnknownValueError:
            print("Was nable to recognize what said.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition; {e}")
