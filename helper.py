def map_input(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def check_deadzone(controller_value, deadzone):
  if abs(controller_value) < deadzone:
    return 0.0
  else:
    return controller_value 