#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor,right_motor,87,130 )

# Notes:
# robot.straight(300), use ruler to measure the distance in cm and then multiply by 10 to get mm
# robot.turn(90) = makes robot turn right/left (no need to add degrees)
# Since robot is built backwards, makes robot.straight codes to go negatively and vise versa for moving robot backwards 
# Make robot.turn code negative for moving right and postive for left 

# Write your program here.
robot.straight(-600)
robot.turn(-30)
robot.straight(-40)
#robot.straight(-750)
#robot.turn(-45)
#robot.straight(-1050)
#robot.turn(-90)
#robot.straight(-150)
