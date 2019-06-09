import turtle
import math
import sys
import random
import time
turtle.setup(width = 1000, height = 1000, startx = 0, starty = 0)
rocket = turtle.Turtle()
rocket.shape('circle')
rocket.shapesize(0.005)
rocket.color('red')
rocket.pu()
hole = turtle.Turtle()
hole.color('black')
hole.shapesize(0.1)
hole.shape('circle')
hole.penup()
O = 0
l = 2.898
r = 300
a = 0.998
vr = 0
rocket.goto(math.cos(O)*r,math.sin(O)*r)
rocket.pd()
rocket.speed(0)
while r>1:
    accelr=-0.1*(r*(((1/r**4)*(r**2-2*l**2*r+3*l**2))))
    vO=(l/(r**2+a**2+(a**2*r)/(r**2)))
    vr+=accelr
    r+=r*vr
    O+=r*vO
    rocket.goto(math.cos(O)*r,math.sin(O)*r)
