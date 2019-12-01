import cv2


class CaptureFrame:

    def __init__(self, video):
        self.video = video

    def startCapturing(self):
        while True:
            check, frame = self.video.read()
            cv2.imshow("Webcamera", frame)
            key = cv2.waitKey(1)
            if key == ord('s'):
                break
        pic = cv2.imwrite("Image.jpg", frame)
        self.destructor()

    def cameraDestructor(self):
        self.video.release()
        cv2.destroyAllWindows


video = cv2.VideoCapture(0)
capture = CaptureFrame(video)
capture.startCapturing()


