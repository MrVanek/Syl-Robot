from time import sleep
from adafruit_motorkit import MotorKit
kit = MotorKit()

class Robot():

  def __init__(self):
    print("Initializing robot...")
    

  def forward(self, amount, speed = 0.5):
    print("Moving Forward")
    self.move_left_side(speed)
    self.move_right_side(speed)
    sleep(amount)
    self.full_stop()    


  def back(self, amount, speed = 0.5):
    print("Moving Backwards")
    self.move_left_side(-speed)
    self.move_right_side(-speed)
    sleep(amount)
    self.full_stop()    


  def right(self, amount, speed = 0.5):
    print("Turning Right")
    self.move_left_side(speed)
    self.move_right_side(-speed)
    sleep(amount)
    self.full_stop()    


  def left(self, amount, speed = 0.5):
    print("Turning Left")
    self.move_left_side(-speed)
    self.move_right_side(speed)
    sleep(amount)
    self.full_stop()    


  def move_left_side(self, power = 0.5):
    kit.motor3.throttle = power
    kit.motor4.throttle = power


  def move_right_side(self, power = 0.5):
    kit.motor1.throttle = power
    kit.motor2.throttle = power


  def full_stop():
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0

