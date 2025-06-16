# pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Inicializar ladrillo y dispositivos
ev3 = EV3Brick()
motorA = Motor(Port.B)
motorB = Motor(Port.C)
sensor_color = ColorSensor(Port.S3)


motorA.run(300)
motorB.run(300)


while 1==1:
    if sensor_color.color() == Color.RED:

        motorA.stop()
        motorB.stop()

        ev3.speaker.beep()

        wait(1000)

        motorA.run_time(-300, 1000)
        motorB.run_time(-300, 1000)

        break  

    wait(100)