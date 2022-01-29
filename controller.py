from evdev import InputDevice, categorize, ecodes, KeyEvent

class Controller ():
  def __init__(self):
    gamepad = InputDevice('/dev/input/event1')
    self.using_gamepad = True
    print(gamepad)
    self.begin_controlling()


  def begin_controlling(self):
    if self.using_gamepad:
      for event in self.gamepad.read_loop():
        if event.type == 3 and event.code == 5:
          print(event.value)

        '''
        print(categorize(event))
        
        if event.type == ecodes.EV_KEY:
          keyevent = categorize(event)
          if keyevent.keystate == KeyEvent.key_down:
            if keyevent.scancode == 305:
                print('Back')
            elif keyevent.scancode == 304:
                print ('Left')
            elif keyevent.scancode == 307:
                print ('Forward')
            elif keyevent.scancode == 306:
                print ('Right')
        '''

