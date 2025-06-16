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
ev3 = EV3Brick()
color_sensor = ColorSensor(Port.S3) 

# Write your program here.
ev3.speaker.beep()

mA = Motor(Port.B)
mB = Motor(Port.C)

tiempo_recorrido
color_detectado = color_sensor.color()
color_objetivo = Color.RED

mA.run(-300)
mB.run(-300)

while color_detectado=color_objetivo:
    if color_detectado == color_objetivo:    
        break()
        color = color_sensor.color()
    sleep(0.1)
mA.run(tiempo_recorrido)
mB.run(tiempo_recorrido)