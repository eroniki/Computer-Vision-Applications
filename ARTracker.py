
from FrameCapturing import CaptureFrame

if __name__ == '__main__':
    settings = {"show": True,
                "verbose": 2,
                "video": 0,
                "root_path": "figures/"}

    myTracker = CaptureFrame.ARTracker(settings)
    myTracker()
