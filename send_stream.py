from button_class import buttonRpi
from camera_class import Camera
from server_class import Server

cam = Camera()
serv = Server()

def gen(camera):
    frame = camera.get_frame()
    yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def button_callback(channel):
    while serv.send_request('gen(cam)') != 500:
        pass

if __name__ == '__main__':
    btn = buttonRpi(37, button_callback)
    try:
        while(1): pass
    except KeyboardInterrupt:
        pass
