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
color_sensor = ColorSensor(Port.1)

# Couleurs RGB  - mesurés avec print(color_sensor.rgb())
yellow = (55, 33, 38)
blue = (23, 54, 153) 

def same_color_as(rgb_target: (int, int, int)) -> bool:
    """
    Compare les valeurs rgb du capteur avec une couleur de référence, 
    rgb_target, qui est un tuple (r, g, b).

    Retourne False si au moins une des valeurs mesurées dans rgb_measured 
    est trop différente de la valeur de référence correspondante dans 
    rgb_target.

    Sinon retourne True
    """
    rgb_measured = color_sensor.rgb()
    err = 5 # écart acceptable

    for i in range(2):
        if abs(rgb_target[i] - rgb_measured[i]) >= err :
            return False
    return True


# Write your program here.
while True :
    if same_color_as(yellow) :
        ev3.speaker.say("yellow")
    elif same_color_as(blue) :
        ev3.speaker.say("blue")
    wait(10)