from flask import Flask, render_template, Response
from src.finger_count.finger_captcha import FingerCAPTCHA
from src.finger_count.video_capture import VideoCapture

app = Flask(__name__)


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
@app.route("/finger-count")
def finger_count():
    return render_template("finger_count.html")


@app.route("/finger-count/video")
def video():
    vc = VideoCapture()
    captcha = FingerCAPTCHA()
    return Response(
        vc(captcha.run), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


# * Word reading.
# * Finger counting.
@app.route("/word-reading")
def word_reading():
    return render_template("word_reading.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
