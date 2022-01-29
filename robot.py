from time import sleep
from adafruit_motorkit import MotorKit
kit = MotorKit()

class Robot():

  def __init__(self):
    print("Initializing robot...")

  def forward(self, amount):
    print("Trying to Move Motor")
    kit.motor1.throttle = 0.5
    sleep(2)
    kit.motor1.throttle = 0.0


  def back(self, amount):
    pass

  def right(self, amount):
    pass

  def left(self, amount):
    pass