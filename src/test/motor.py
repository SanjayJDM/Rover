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

try:
 while True:
  x = raw_input()
  print x
  if (x == 'w'):
   Forwards()
  if (x == 's'):
   Backwards()
  if (x == 'a'):
   Left()
   time.sleep(0.5)
  if (x == 'd'):
   Right()
   time.sleep(0.5)
  if (x == 'x')
   StopMotors()

except KeyboardInterrupt:
  print "QUIT"
  GPIO.cleanup()
