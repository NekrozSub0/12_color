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
ma = Motor (Port. A)
mc = Motor (Port. C)
sensor_color =ColorSensor (Port.s3)
ColorSensor.reflection
robot =DriveBase(mA, mC, 55.5, 104)
if sensor_color==color.BLACK
    print("Color negro")
    if sensor_color.reflection>50%
    print("menor de 50")
    if sensor_color.reflection<50%
    print("mayor de 50")

# Write your program here.
ev3.speaker.beep()
