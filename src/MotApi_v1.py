from flask import Flask
from flask import json
#from flask_api import FlaskAPI
import RPi.GPIO as GPIO
import time # Import the Time library
# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Set variables for the GPIO motor pins 
pinMotorAForwards = 10 
pinMotorABackwards = 9 
pinMotorBForwards = 8 
pinMotorBBackwards = 7
# Set the GPIO Pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

#app = FlaskAPI(__name__)
app = Flask(__name__)

@app.route('/', methods=["GET"])

# Turn all motors off
def StopMotors():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)
# Turn both motors forwards
def Forwards():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)
# Turn both motors backwards
def Backwards():
   GPIO.output(pinMotorAForwards, 0) 
   GPIO.output(pinMotorABackwards, 1) 
   GPIO.output(pinMotorBForwards, 0) 
   GPIO.output(pinMotorBBackwards, 1)
# Turn left
def Left():
   GPIO.output(pinMotorAForwards, 0) 
   GPIO.output(pinMotorABackwards, 1) 
   GPIO.output(pinMotorBForwards, 1)
   GPIO.output(pinMotorBBackwards, 0)
# Turn Right
def Right():
   GPIO.output(pinMotorAForwards, 1) 
   GPIO.output(pinMotorABackwards, 0) 
   GPIO.output(pinMotorBForwards, 0) 
   GPIO.output(pinMotorBBackwards, 1)

def api_root():
    return {
           "url": request.url 
                         }  
@app.route('/sanjayrover/fwd/', methods=["GET", "POST"])
def api_fwds_control():
    Forwards()
    response = app.response_class(
        response=json.dumps("FORWARD ACTION"),
        status=200,
        mimetype='application/json'
    )
    return response
@app.route('/sanjayrover/back/', methods=["GET", "POST"])
def api_bck_control():   
    Backwards()
    response = app.response_class(
        response=json.dumps("BACKWARD ACTION"),
        status=200,
        mimetype='application/json'
    )
    return response
@app.route('/sanjayrover/stop/', methods=["GET", "POST"])
def api_stp_control():
    StopMotors()
    response = app.response_class(
        response=json.dumps("STOPPING ALL ACTIONs"),
        status=200,
        mimetype='application/json'
    )
    return response
@app.route('/sanjayrover/right/', methods=["GET", "POST"])
def api_right_control():
    Right()
    response = app.response_class(
        response=json.dumps("RIGHT ACTION"),
        status=200,
        mimetype='application/json'
    )
    return response
@app.route('/sanjayrover/left/', methods=["GET", "POST"])
def api_left_control():
    Left()
    response = app.response_class(
        response=json.dumps("LEFT ACTION"),
        status=200,
        mimetype='application/json'
    )
    return response
@app.route('/sanjayrover/hc/', methods=["GET"])
def api_hc():
   response = app.response_class(
       response=json.dumps("SERVER STATUS OK"),
       status=200,
       mimetype='application/json'
   )
   return response
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

