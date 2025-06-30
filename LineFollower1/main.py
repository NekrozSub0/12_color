#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = EV3Brick()
ev3.speaker.beep()
MR=Motor(Port.A)
ML=Motor(Port.D)
color_sensor=ColorSensor(Port.S1)
robot=DriveBase(ML,MR,wheel_diameter=55.5,axle_track=104)

while color_sensor.reflection()!=90:
    reflect=color_sensor.reflection()
    if reflect<60:
        robot.drive(20,-50)
        wait(300)
    elif reflect>60:
        robot.drive(20,50)
        wait(300)
    ev3.screen.clear()
    ev3.screen.print(reflect)
    wait(200)
