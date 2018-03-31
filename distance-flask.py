#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os
from flask import Flask

app = Flask(__name__)


# initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(18,GPIO.IN)

def checkdist():
        GPIO.output(16, GPIO.HIGH)
        time.sleep(0.000015)
        GPIO.output(16, GPIO.LOW)
        while not GPIO.input(18):
                pass
        t1 = time.time()
        while GPIO.input(18):
                pass
        t2 = time.time()
        return (t2-t1)*340/2

@app.route('/')
def mainmenu():
    PIval = checkdist()
    PIval = "%0.2f" %PIval
    return """
    <html><body>
    <center><h1>BETA version of my home automation system<br/>
        <h2><u>The latest reading of the light sensor is: {0}<br>
    </center>
    </body></html>
    """.format(PIval)

if __name__ == "__main__":

        app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
