from button_class import buttonRpi
from camera_class import Camera
from server_class import Server

cam = Camera()
serv = Server()

def gen(camera):
    frame = camera.get_frame()
    return frame

def button_callback(channel):
    if cam.isOpened():
        return;
    
    location = serv.get_response()
    if location == None:
        return;
    serv.set_location(location)
    
    cam.init()
    cam.start()

    while serv.send_request(gen(cam)) != 500:
        pass
    print("\n>transmition terminated")

    cam.release()
   

if __name__ == '__main__':
    btn = buttonRpi(37, button_callback)
    btn.set_event()

    print("\n>ready")
    try:
        while(1): pass
    except KeyboardInterrupt:
        pass

    del cam
    del btn
