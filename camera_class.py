import cv2

class Camera(object):
    def __init__(self):
        if cv2.__version__.startswith('2'):
            PROP_FRAME_WIDTH = cv2.cv.CV_CAP_PROP_FRAME_WIDTH
            PROP_FRAME_HEIGHT = cv2.cv.CV_CAP_PROP_FRAME_HEIGHT
        elif cv2.__version__.startswith('3'):
            PROP_FRAME_WIDTH = cv2.CAP_PROP_FRAME_WIDTH
            PROP_FRAME_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT
        elif cv2.__version__.startswith('4'):
            PROP_FRAME_WIDTH = cv2.CAP_PROP_FRAME_WIDTH
            PROP_FRAME_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT

        self.cap = cv2.VideoCapture(0)
        self.cap.release()
        self.cap.set(PROP_FRAME_WIDTH, 320)
        self.cap.set(PROP_FRAME_HEIGHT, 240)

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        success, image = self.cap.read()
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 60]
        ret, jpeg = cv2.imencode('.jpg', image, encode_param)
        return jpeg.tostring()

    def init(self):
        self.cap = cv2.VideoCapture(0)

    def release(self):
        self.cap.release()

    def isOpened(self):
        return self.cap.isOpened()

    def start(self):
        for i in range(4): self.cap.read()
