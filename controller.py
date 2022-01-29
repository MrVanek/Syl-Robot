from evdev import InputDevice, ecodes, categorize, KeyEvent

class Controller ():
  def __init__(self):
    self.gamepad = InputDevice('/dev/input/event0')
    self.using_gamepad = True
    print(self.gamepad)
    self.begin_controlling()


  def begin_controlling(self):
    if self.using_gamepad:
      for event in self.gamepad.read_loop():

        #Check for axis events
        if event.type == ecodes.EV_ABS:        
          # Check for left stick Y
          # TODO: normalize this value from -1 to 1
          # TODO: use it to drive the robot
          if event.code == ecodes.ABS_Y:
            print (event.value)


        # This is a button example.  scancode probably incorrect.   
        if event.type == ecodes.EV_KEY:
          keyevent = categorize(event)
          if keyevent.keystate == KeyEvent.key_down:
            if keyevent.scancode == 305:
                print('Back')
        
        
        # TODO Get a key value to full stop and drop out of the program.
      

