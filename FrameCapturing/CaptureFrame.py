import cv2
import matplotlib.pyplot as plt

class ARTracker:
    def __init__(self, settings):
        self.video = cv2.VideoCapture(settings["video"])
        if self.video.isOpened() is False:
            raise IOError("Video is not found!")

    def __del__(self):
        self.video.release()
        cv2.destroyAllWindows
        plt.close()

    def __call__(self):
        '''Design the process here.'''
        while True:
            _, frame = self.readImage()
            if ARTracker.showImage(frame) is not True:
                break

    def readImage(self):
        check, frame = self.video.read()
        return check, frame

    @staticmethod
    def showImage(img):
        try:
            cv2.imshow("Webcamera", img)
            key = cv2.waitKey(1)
            if key == ord('s'):
                print("Quitting...")
                return False
        except KeyboardInterrupt as e:
            print("Quitting...")
        except Exception as e:
            print(e)

        return True

    @staticmethod
    def saveImage(path, img):
        cv2.imwrite(path, img)


if __name__ == "__main__":
    pass

