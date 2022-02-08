#https://learn.adafruit.com/mpu6050-6-dof-accelerometer-and-gyro/python-and-circuitpython

import time
import board
import adafruit_mpu6050

class GyroSensor():
  def __init__(self):
    self.i2c = board.I2C()
    self.mpu = adafruit_mpu6050.MPU6050(self.i2c, 68)


  def get_angle(self, axis = 'x', printing = True):
    options = {'x': 0,
               'y': 1,
               'z': 2 }

    angle = self.mpu.gyro[options[axis]]
    if printing:
      print(angle)
    return angle


'''
while True:
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    print("Temperature: %.2f C" % mpu.temperature)
    print("")
    time.sleep(1)
'''
