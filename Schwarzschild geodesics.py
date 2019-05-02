import turtle
import math
import sys
import random
import time
turtle.setup(width = 1000, height = 1000, startx = 0, starty = 0)
rocket = turtle.Turtle()
rocket.shape('circle')
rocket.shapesize(0.05)
rocket.color('red')
rocket.pu()
hole = turtle.Turtle()
hole.color('black')
hole.shapesize(0.2)
hole.shape('circle')
hole.penup()

l = 2
vr = 0
O = 0
r = 35

rocket.goto(math.cos(O)*2*r,math.sin(O)*2*r)
rocket.pd()

while r>1:
    vO=((l)/(0.5*r**2))
    accelr=-(1/r**4)*(r**2-2*l**2*r+3*l**2)
    vr+=accelr
    r+=vr
    O+=vO
    rocket.goto(math.cos(O)*2*r,math.sin(O)*2*r)


    
