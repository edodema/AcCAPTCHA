import cv2 as cv

ds_factor = 0.6


class VideoCamera:
    def __init__(self):
        # capturing video
        self.video = cv.VideoCapture(0)

    def __del__(self):
        # releasing camera
        self.video.release()

    def __call__(self):
        while True:
            _, frame = self.video.read()
            _, jpeg = cv.imencode(".jpg", frame)

            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n\r\n"
            )
