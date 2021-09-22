#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (ColorSensor, GyroSensor, InfraredSensor,
                                 Motor, TouchSensor, UltrasonicSensor)
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import DataLog, StopWatch, wait

# TODO:
# 1. Move the robot in a given number of steps forward, backward, left and right
# 2. Add a color sensor and make it follow a line
# 3. accompolish a small part of the 1st mission (TBD)

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor,right_motor,87,130 )
# we can make new changes

def move(steps, dir):
    # move (fwd/ bk) robot in number of steps indicated in the signature
    if dir is "fwd":
        # move forward
        robot.straight(-1 * steps)
    else if dir is "bk":
        # move backward
        robot.straight(steps)
  
def turn(steps, dir):
    #TODO: turn (left/ right) robot in number of steps indicated in the signature
    if dir is "left":
        robot.turn(steps)
    else if dir is "right":
        robot.turn(-1 * steps)

# Notes:
# robot.straight(300), use ruler to measure the distance in cm and then multiply by 10 to get mm
# robot.turn(90) = makes robot turn right/left (no need to add degrees)
# Since robot is built backwards, makes robot.straight codes to go negatively and vise versa for moving robot backwards 
# Make robot.turn code negative for moving right and postive for left 

# What did we accomplish
# 1. github setup to share code and for version control
# 2. successfully checked in the code into github from visual studio
# 3. Refactored the code to make it more readable and usable
# 4. We came up a plan to complete the mission

# Next steps
# 1. Find out the mission to solve?
# 2. Try this program on the lego and make sure it works
# 3. Write the code to solve small part of the big mission

# Write your program here.
def goto_zone1():
    # Hypothetical mission zone
    move(530,"fwd")
    turn(90, "right")
    move(77, "fwd")
    robot.straight(17)  # move back 17
    # move(17, "bk")
    
    #turn(30,right)
    #turn(40,right)
    #move(40,fwd)
    #move(750,fwd)
    #turn(45,right)
    #move(1050,fwd)
    #turn(90,right)
    #move(150,fwd)

goto_zone1()
#robot.straight(-50
#move(100, "fwd")
# move(100, "bk")
# robot.turn(-30)
# robot.straight(-40)
#robot.straight(-750)
#robot.turn(-45)
#robot.straight(-1050)
#robot.turn(-90)
#robot.straight(-150)
