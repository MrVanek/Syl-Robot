from evdev import InputDevice, categorize, ecodes

class Controller ():
  def __init__(self):
    gamepad = InputDevice('/dev/input/event1')
    using_gamepad = True
    print(gamepad)

    for event in gamepad.read_loop():
      print(categorize(event))

