from flask import Flask, render_template, Response

from src.finger_count.finger_captcha import FingerCAPTCHA
from src.finger_count.video_capture import VideoCapture

from src.image_classification.image_classification import ImageCAPTCHA
from src.text_recognition.text_recognition import TextCAPTCHA

# TODO Maybe add parsing options and pass them to constructors
#  rather than always using default values

app = Flask(__name__)
# ! Refresh does not change the ground truth, move that into video(), yet it yields the wrong JSON reading.
finger_captcha = FingerCAPTCHA()
# image_captcha = ImageCAPTCHA()


@app.route("/")
def main() -> str:
    """Home window.

    Returns:
        str: HTML code.
    """
    return render_template("index.html")


@app.route("/configure")
def configure() -> str:
    """Window in which we configure the user's abilities.

    Returns:
        str: HTML code.
    """
    return render_template("configure.html")


# * Finger counting.
@app.route("/finger_count")
def finger_count():
    return render_template("finger_count.html")


@app.route("/finger_count/video")
def video():
    vc = VideoCapture()
    return Response(
        vc(finger_captcha.run), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


# * Image classification.
@app.route("/image_classification")
def image_classification():
    image_captcha = ImageCAPTCHA()
    return render_template("image_classification.html")


# * Text recognition.
@app.route("/text_recognition")
def text_recognition():
    text_captcha = TextCAPTCHA()
    return render_template("text_recognition.html")


# * Word reading.
# @app.route("/wordreading")
# def word_reading():
#     return render_template("word_reading.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
