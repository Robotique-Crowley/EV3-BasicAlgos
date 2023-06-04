#!/usr/bin/env pybricks-micropython

"""
Idéalement testez ce code avec un seul moteur auquel vous avez attaché un
long poutre. Comme ça, le bras bloquera sur le corp du moteur dans les deux
directions (ou sur votre main).

C'EST IMPORTANT DE NE PAS OPÉRER UN MOTEUR LORSQU'IL EST BLOQUÉ
    Ça peut endommager le moteur et d'autres parties du robot

    > Le code dans ces exemples vous aide à prévenir les dommages potentiels
"""

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
motor = Motor(Port.A)


# Constantes
SPEED = 300


# Fonctions
def stall_example() :
    """
    Cet exemple utilise run_until_stalled pour opérer le moteur afin
    de trouver la limite de sa rotation sans le forcer plus loin.
    Par la suite, on revient à la position zéro et on retourne juste avant
    l'angle limite détecté.
    """
    motor.reset_angle(0)
    print(motor.angle())
    # avancer jusqu'à la limite et garder l'angle dans une variable
    stall_angle = motor.run_until_stalled(SPEED, then = Stop.HOLD, duty_limit = 75)
    print(stall_angle)
    ev3.speaker.beep()
    wait(1000)
    # revient à l'angle 0
    motor.run_target(-SPEED, 0)
    ev3.speaker.beep()
    wait(200)
    # retourne jusqu'à la limite du mouvement
    motor.run_target(SPEED, 0.95 * stall_angle)
    ev3.speaker.beep()

def manual_stall() :
    """
    Voici une autre façon de faire la même chose que dans stall_example
    mais en tournant le moteur dans l'autre direction (-SPEED)
    """
    motor.reset_angle(0)
    print(motor.angle())
    # avancer jusqu'à la limite et garder l'angle dans une variable
    while True  :
        motor.run(-SPEED)
        wait(60)
        if (motor.speed() == 0) :
            motor.hold()
            break
    stall_angle = motor.angle()
    print(stall_angle)
    ev3.speaker.beep()
    wait(1000)
    # revient à l'angle 0
    motor.run_target(SPEED, 0)
    ev3.speaker.beep()
    wait(200)
    # retourne jusqu'à la limite du mouvement
    motor.run_target(-SPEED, 0.95 * stall_angle)
    ev3.speaker.beep()



# Write your program here.
ev3.speaker.beep()

stall_example()
manual_stall()