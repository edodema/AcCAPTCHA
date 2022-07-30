from flask import Flask, render_template, Response
from src.finger_count.tmp import VideoCamera

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
# @app.route("/finger-count")
# def video():
#     return render_template("finger_count.html")


# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")


# @app.route("/video_feed")
# def video_feed():
#     return Response(
#         gen(VideoCamera()), mimetype="multipart/x-mixed-replace; boundary=frame"
#     )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
