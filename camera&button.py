# Button class was written by Andrew Kiselev

# USAGE btn - buttonRpi object
#       btn = buttonRpi(optional args: pinNumber, callback_function)
#
#       Use this decloration for callback func
#           def callback_function(channel):
#               ...
#
#       btn.set_event() - set callback on push event
#       btn.get_state() - get state of button (0/False/GPIO.LOW or
#                                               1/True/GPIO.HIGH)
#       btn.clean() -   clean all GPIO pins
#import RPi.GPIO as GPIO
import time
import cv2
from flask import Flask, render_template, Response
import requests

#from button_class import buttonRpi
from camera_streaming import Camera


#btn = buttonRpi(37, new_callback_btn)
#event_from_button = btn.get_state()
server_adress = 'https://intelligent-nurse.azurewebsites.net/'
test_adress = 'http://localhost:5000'

# if event getted push frame date into server
def server_rqs(server_adress):
    r = requests.get(server_adress)
    if (int(r.status_code) == 200):
        return True
    else:
        return False

def run_pushing(event_from_button, server_adress):
    if event_from_button == True:
        app = Flask(__name__)

        @app.route('/')
        def index(): return render_template('stream.html')

        def gen(camera):
            while (server_rqs(server_adress)):
                frame = camera.get_frame()
                _, frame_encoded = cv2.imencode('.jpg', frame)
                yeld(b'--frame\r\n'
                     b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        @app.route('video_feed')
        def video_feed():
            return Response(
            gen(Camera()),
            mimetype='multipart/x-mixed-replace; boundary=frame'
            )
        # For rinning on Gosha's server inser host, port
        app.run(host='0.0.0.0', port=80, debug=True)
    else:
        print('Press the button to start streaming')
