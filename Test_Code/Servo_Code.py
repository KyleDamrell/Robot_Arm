## This is the code for controlling a servo on a raspberry pi:
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time

################################
# RPi and Motor Pre-allocations
################################
#
#define GPIO pins
direction_black= 22 # Direction (DIR) GPIO Pin
step_black = 23 # Step GPIO Pin
EN_pin_black = 24 # enable pin (LOW to enable)

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction_black, step_black, (21,21,21), "DRV8825")
GPIO.setup(EN_pin_black,GPIO.OUT) # set enable pin as output

###########################
# Actual motor control
###########################
#
GPIO.output(EN_pin_black,GPIO.LOW) # pull enable to low to enable motor
mymotortest.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                     "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                     6400, # number of steps
                     .00001, # step delay [sec]
                     True, # True = print verbose output
                     .00001) # initial delay [sec]

GPIO.cleanup() # clear GPIO allocations after run

# Red
direction_red = 19 # Direction (DIR) GPIO Pin
step_red = 16 # Step GPIO Pin
EN_pin_red = 20 # enable pin (LOW to enable)

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction_red, step_red, (21,21,21), "DRV8825")
GPIO.setup(EN_pin_red,GPIO.OUT) # set enable pin as output

print ("Done Black")

# ###########################
# # Actual motor control
# ###########################
# #
# GPIO.output(EN_pin_red,GPIO.LOW) # pull enable to low to enable motor
# mymotortest.motor_go(False, # True=Clockwise, False=Counter-Clockwise
#                      "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
#                      200, # number of steps
#                      .0005, # step delay [sec]
#                      False, # True = print verbose output
#                      .0001) # initial delay [sec]
# 
# print ("Done Red")