import turtle
import math
import sys
turtle.setup(width = 1000,height = 1000,startx = 0, starty = 0)
planet1 = turtle.Turtle()
planet1.color('darkgreen')
planet1.shapesize(6)
planet1.shape('circle')
moon = turtle.Turtle()
moon.color('blue')
moon.shapesize(1.75)
moon.shape('circle')
moon.penup()
rocket =  turtle.Turtle()
rocket.penup()
turtle.tracer(2)
vx1 = 3
vy1 = 0
x1 = 0
y1 = 400
moon.goto(x1,y1)
moon.penup()
moon.speed(0.5)
vx3 = vx1/(4000/-660)
vy3 = vy1/(4000/-660)
x3 = 0
y3 = 0 
planet1.speed(0.5)
planet1.penup()
planet1.goto(x3,y3)
vx5 = 6
vy5 = 0.25
x5 = 0
y5 = 100
rocket.goto(x5,y5) 
rocket.speed(0.5)
vxm = 0
vym = 0
def gravity():
  global x1
  global y1
  global x3
  global y3
  global x5
  global y5
  global vx1
  global vy1
  global vx3
  global vy3
  global vx5
  global vy5
  global vxm
  global vym
  while True:
    gravity1 = (((4000)/moon.distance(planet1)**2))    
    gravity2 = (((20)/moon.distance(rocket)**2))    
    angle1 = math.atan2(moon.ycor()-planet1.ycor(),moon.xcor()-planet1.xcor())
    angle2 = math.atan2(moon.ycor()-rocket.ycor(),moon.xcor()-rocket.xcor())
    accel_x1 = gravity1*math.cos(angle1)*-1 
    accel_y1 = gravity1*math.sin(angle1)*-1
    accel_x2 = gravity2*math.cos(angle2)*-1 
    accel_y2 = gravity2*math.sin(angle2)*-1   
    vx1 += accel_x1+accel_x2
    vy1 += accel_y1+accel_y2
    gravity3 = (((660)/planet1.distance(moon)**2))     
    gravity4 = (((20)/planet1.distance(rocket)**2))     
    angle3 = math.atan2(planet1.ycor()-moon.ycor(),planet1.xcor()-moon.xcor())
    angle4 = math.atan2(planet1.ycor()-rocket.ycor(),planet1.xcor()-rocket.xcor())
    accel_x3 = gravity3*math.cos(angle3)*-1 
    accel_y3 = gravity3*math.sin(angle3)*-1
    accel_x4 = gravity4*math.cos(angle4)*-1 
    accel_y4 = gravity4*math.sin(angle4)*-1   
    vx3 += accel_x3+accel_x4
    vy3 += accel_y3+accel_y4
    gravity5 = (((4000)/rocket.distance(planet1)**2))         
    gravity6 = (((660)/rocket.distance(moon)**2))      
    angle5 = math.atan2(rocket.ycor()-planet1.ycor(),rocket.xcor()-planet1.xcor())
    angle6 = math.atan2(rocket.ycor()-moon.ycor(),rocket.xcor()-moon.xcor())
    accel_x5 = gravity5*math.cos(angle5)*-1  
    accel_y5 = gravity5*math.sin(angle5)*-1  
    accel_x6 = gravity6*math.cos(angle6)*-1 
    accel_y6 = gravity6*math.sin(angle6)*-1  
    vx5 += accel_x5+accel_x6
    vy5 += accel_y5+accel_y6
    while moon.distance(planet1) <= 60:
      turtle.done()
      sys.exit()
    while rocket.distance(planet1) <= 60: 
      vx5 = 0
      vy5 = 0
      turtle.bye()
      sys.exit()
    while rocket.distance(moon) <= 17.499:
      vx5 = 0
      vy5 = 0
      turtle.bye()
      sys.exit()
    y1 += vy1
    x1 += vx1
    moon.goto(x1,y1)
    y3 += vy3
    x3 += vx3
    planet1.goto(x3,y3)
    y5 += vy5 + vym
    x5 += vx5 + vxm
    rocket.goto(x5,y5) 
    
def keys():
  turtle.listen()
  turtle.onkey(right,'d')
  turtle.onkey(left,'a')
  turtle.onkey(up,'w')
  turtle.onkey(down,'s')
  turtle.onkey(leave,'x')

def leave():
  turtle.bye()
  sys.exit()


def right():
  global x5
  global vxm
  vxm += 0.25
  x5 += vxm 
def up():
  global y5
  global vym
  vym += 0.25  
  y5 += vym
def down():
  global y5
  global vym
  vym -= 0.25  
  y5 += vym
def left():
  global x5
  global vxm
  vxm -= 0.25
  x5 += vxm

keys() 
gravity()  
 
  
  
