from flask import Flask, render_template, Response
from src.finger_count.tmp import VideoCamera
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
def video():
    return render_template("finger_count.html")


@app.route("/video_feed")
def video_feed():
    vc = VideoCapture(web=True)
    captcha = FingerCAPTCHA()
    return Response(
        vc(captcha.run), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
