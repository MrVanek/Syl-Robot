from evdev import InputDevice

class Controller ():
  def __init__(self):
    gamepad = InputDevice('/dev/input/event1')
    using_gamepad = True
    print(gamepad)

