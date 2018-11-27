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


import RPi.GPIO as GPIO
import time

class buttonRpi:

    pin = 37
    callback_func = None

    def __init__(self, pin=37, callback_func=None):
        self.pin = pin
        self.callback_func = self.button_callback
        if callback_func:
            self.callback_func = callback_func
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
    def button_callback(self, channel):
        print("Button was pushed!")

    def set_event(self):
        GPIO.add_event_detect(self.pin, GPIO.RISING, 
                                callback=self.callback_func)

    def get_state(self):
        res=GPIO.input(self.pin)
        if res:
            time.sleep(.200)
        return res

    def clean(self):
        GPIO.cleanup()
