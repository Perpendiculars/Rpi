from time import time

class Camera(object):
    def __init__(self):
        self.frames = [open("static/" + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    def get_frame(self):
        return self.frame[int(time()) % 3]
