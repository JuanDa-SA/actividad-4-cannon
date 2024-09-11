"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

"""Importamos libreria para el cambio de colores. Autor: Javier J.P."""
import random 
from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

"""Creamos el cambio de colores. Autor: Javier J.P."""
color1 = random.choice(['purple', 'green', 'yellow', 'brown'])

"""Creamos otro cambio de colores. Autor: Javier J.P."""
color2 = random.choice(['red', 'cian', 'pink', 'blue'])

def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()
    
    """Creamos el cambio de forma de los proyectiles. Autor:Javier J.P."""
    shape('square')

    for target in targets:
        goto(target.x, target.y)
        """Cambio de color de los objetivos. Autor: Javier J.P."""
        dot(20, color1)

    if inside(ball):
        goto(ball.x, ball.y)
        """Cambio de color y de forma de los balones. Autor: Javier J.P."""
        color(color2)
        stamp()

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)


    """Cambia la velocidad de los objetivos. Autor: Alberto"""
    for target in targets:
        target.x -= 2

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    "Solamente si el objetivo sale de la pantalla lo ponemos del lado derecho en el eje de las x. Autor: Juan Daniel"
    for target in targets:
        if not inside(target):
            target.x = 200


    """Cambia la velocidad de todo el juego (proyectil y objetivos). Autor: Alberto"""
    ontimer(move, 20)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
