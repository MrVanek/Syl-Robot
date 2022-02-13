
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
    self.full_stop()
    print(self.gamepad)
    if self.using_gamepad:
      self.begin_controlling()
    

  def forward(self, amount = 1, speed = 0.5):
    print("Moving Forward")
    self.move_left_side(speed)
    self.move_right_side(speed)
    if not self.using_gamepad:
      sleep(amount)
      self.full_stop()    


  def back(self, amount = 1, speed = 0.5):
    print("Moving Backwards")
    self.move_left_side(-speed)
    self.move_right_side(-speed)
    if not self.using_gamepad:
      sleep(amount)
      self.full_stop()    


  def right(self, amount = 1, speed = 0.75):
    print("Turning Right")
    self.move_left_side(speed)
    self.move_right_side(-speed)
    if not self.using_gamepad:
      sleep(amount)
      self.full_stop()    


  def left(self, amount = 1, speed = 0.75):
    print("Turning Left")
    self.move_left_side(-speed)
    self.move_right_side(speed)
    if not self.using_gamepad:
      sleep(amount)
      self.full_stop()    


  def move_left_side(self, power = 0.5):
    kit.motor3.throttle = power
    kit.motor4.throttle = power


  def move_right_side(self, power = 0.5):
    kit.motor1.throttle = -power
    kit.motor2.throttle = -power


  def full_stop(self):
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 0.0
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0


  def begin_controlling(self):
    if self.using_gamepad:
      for event in self.gamepad.read_loop():

        #Check for LEFT STICK axis events
        if event.type == ecodes.EV_ABS:        
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

          # TODO: use inputs to drive robot
          self.movement_logic(forward_speed, turn_speed)


        # This is a button example.  scancode probably incorrect.   
        if event.type == ecodes.EV_KEY:
          keyevent = categorize(event)
          if keyevent.keystate == KeyEvent.key_down:
            if keyevent.scancode == 305:
                print('Circle')
        
        
        # TODO Get a key value to full stop and drop out of the program.
      
  def movement_logic(self, forward_speed, turn_speed):
    
    # No input
    if (forward_speed == 0.0 and turn_speed == 0.0):
      self.full_stop()
    
    # Turn only
    elif(forward_speed == 0.0):
      if (turn_speed > 0.0):
        self.right(speed = turn_speed)
      else:
        self.left(speed = turn_speed)
    
    # Straight only
    elif(turn_speed == 0.0):
      if (forward_speed > 0.0):
        self.forward(speed = forward_speed)
      else:
        self.back(speed = forward_speed)

    # Angled Drive
    else:
      pass
      #power sides independantly

