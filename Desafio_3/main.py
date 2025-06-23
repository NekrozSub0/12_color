#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import array

ev3 = EV3Brick()

# Write your program here.
ev3.speaker.beep()  

motorA=Motor(Port.B)
motorB=Motor(Port.C)
sensor_color=ColorSensor(Port.S3)
motorA.run(50)
motorB.run(50)
contador=0

while 1==1:
    if sensor_color.color()==Color.BLACK:
        contador=contador+1
        wait(50)
        print("negro")
        print(contador) 
    if sensor_color.color()==Color.WHITE:
        contador=0
        if contador > 30:
            break

print("Bucle roto")
wait(500)

motorA.stop
motorB.stop

print("El contador de negro detectado da: ")
print(contador)

ev3.screen.clear()
ev3.screen.print("El contador de negro detectado da: ")
ev3.screen.print(contador)
wait(3000)

print(contador)