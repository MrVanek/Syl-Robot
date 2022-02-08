#from robot import Robot
from time import sleep
from gyro import GyroSensor
#from controller import Controller
#  This will be the repo to get the 6 wheeled robot working with Sylvie
#192.168.0.148

# Steps:  
# 1. Get Motor Hat to move a motor  DONE
# 2. Get all motors set up and driving forward and backwards based on code
# 3. Turning
# 4. Controller mechanism (Bluetooth game controller or usb?) STARTED



# Setup

# if using_gamepad = FALSE, Main Program will run
# if using_gamepad = TRUE, You can control the robot via usb controller
gyro = GyroSensor()

while True:
  gyro.get_angle()
'''
jj = Robot(using_gamepad = True)


# Main Program
jj.forward(2)
sleep(1)
jj.back(2)
sleep(1)
jj.right(2)
sleep(1)
jj.left(2)

'''