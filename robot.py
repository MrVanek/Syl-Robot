from time import sleep
from adafruit_motorkit import MotorKit
from evdev import InputDevice, ecodes, categorize, KeyEvent
from helper import map_input, check_deadzone

kit = MotorKit()

class Robot():

  def __init__(self, using_gamepad = True):
    print("Initializing robot...")
    self.MAX_AXIS_VALUES = 32768
    self.DEADZONE = 0.15
    self.gamepad = InputDevice('/dev/input/event0')
    self.using_gamepad = using_gamepad
    print(self.gamepad)
    if self.using_gamepad:
      self.begin_controlling()
    

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


  def full_stop(self):
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0


  def begin_controlling(self):
    if self.using_gamepad:
      for event in self.gamepad.read_loop():

        #Check for axis events
        if event.type == ecodes.EV_ABS:        
          # Check for left stick Y
          # TODO: normalize this value from -1 to 1
          # TODO: use it to drive the robot
          forward_speed = 0.0
          turn_speed = 0.0
          if event.code == ecodes.ABS_Y:
            speed = map_input(event.value, self.MAX_AXIS_VALUES, -self.MAX_AXIS_VALUES, -1, 1)
            forward_speed = check_deadzone(speed, self.DEADZONE)
            #print (forward_speed)

          if event.code == ecodes.ABS_X:
            speed = map_input(event.value, self.MAX_AXIS_VALUES, -self.MAX_AXIS_VALUES, -1, 1)
            turn_speed = check_deadzone(speed, self.DEADZONE)
            print (turn_speed)

          self.movement_logic(forward_speed, turn_speed)


        # This is a button example.  scancode probably incorrect.   
        if event.type == ecodes.EV_KEY:
          keyevent = categorize(event)
          if keyevent.keystate == KeyEvent.key_down:
            if keyevent.scancode == 305:
                print('Back')
        
        
        # TODO Get a key value to full stop and drop out of the program.
      
  def movement_logic(self, forward_speed, turn_speed):
    pass

