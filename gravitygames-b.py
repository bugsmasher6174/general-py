import turtle
import math
import sys
turtle.setup(width = 1000,height = 1000,startx = 0, starty = 0)
planet1 = turtle.Turtle()
planet1.color('darkgreen')
planet1.shapesize(2)
planet1.shape('circle')
turtle.bgcolor('black')
moon = turtle.Turtle()
moon.color('grey')
moon.shapesize(2)
moon.shape('circle')
moon.penup()
rocket =  turtle.Turtle()
rocket.penup()
rocket.shapesize(0.5)
rocket.color('white')
turtle.tracer(2)
moon2 = turtle.Turtle()
moon2.color('cyan')
moon2.shapesize(0.75)
moon2.shape('circle')
moon2.penup()
vx6 = 0
vy6 = 0
vx1 = 1.26
vy1 = 0
x1 = 0
y1 = 30
moon.goto(x1,y1)
moon.penup()
moon.speed(0)
vx5 = -1.6
vy5 = 0
x5 = 0
y5 = 170
rocket.goto(x5,y5) 
rocket.speed(0)
vx8 = -1.05
vy8 = 0
x8 = 0 
y8 = 350
moon2.goto(x8,y8) 
moon2.speed(0)
vx3 = -1.24
vy3 = -0.02
x3 = 0
y3 = -30
planet1.speed(0)
planet1.penup()
planet1.goto(x3,y3)
vxm = 0
vym = 0
def gravity():
  global x1
  global y1
  global x3
  global y3
  global x5
  global y5
  global x8
  global y8
  global vx1
  global vy1
  global vx3
  global vy3
  global vx5
  global vy5
  global vx6
  global vy6 
  global vx8
  global vy8
  global vxm
  global vym
  while True:
    gravity1 = (((10000000000000)/(moon.distance(planet1)*2)**2)*(6.67408*(10**-11)))    
    gravity2 = (((2000000000000)/(moon.distance(moon2)*2)**2)*(6.67408*(10**-11)))    
    angle1 = math.atan2(moon.ycor()-planet1.ycor(),moon.xcor()-planet1.xcor())
    angle2 = math.atan2(moon.ycor()-rocket.ycor(),moon.xcor()-rocket.xcor())
    accel_x1 = gravity1*math.cos(angle1)*-1 
    accel_y1 = gravity1*math.sin(angle1)*-1
    accel_x2 = gravity2*math.cos(angle2)*-1 
    accel_y2 = gravity2*math.sin(angle2)*-1   
    vx1 += accel_x1+accel_x2
    vy1 += accel_y1+accel_y2
    gravity3 = (((10000000000000)/(planet1.distance(moon)*2)**2)*(6.67408*(10**-11)))     
    gravity4 = (((2000000000000)/(planet1.distance(moon2)*2)**2)*(6.67408*(10**-11)))     
    angle3 = math.atan2(planet1.ycor()-moon.ycor(),planet1.xcor()-moon.xcor())
    angle4 = math.atan2(planet1.ycor()-rocket.ycor(),planet1.xcor()-rocket.xcor())
    accel_x3 = gravity3*math.cos(angle3)*-1 
    accel_y3 = gravity3*math.sin(angle3)*-1
    accel_x4 = gravity4*math.cos(angle4)*-1 
    accel_y4 = gravity4*math.sin(angle4)*-1   
    vx3 += accel_x3+accel_x4
    vy3 += accel_y3+accel_y4
    gravity5 = (((10000000000000)/(math.sqrt(math.pow(rocket.xcor()-planet1.xcor(),2) + math.pow(rocket.ycor()-planet1.ycor(),2))*2)**2)*(6.67408*(10**-11)))         
    gravity6 = (((10000000000000)/(math.sqrt(math.pow(rocket.xcor()-moon.xcor(),2) + math.pow(rocket.ycor()-moon.ycor(),2))*2)**2)*(6.67408*(10**-11)))     
    gravity7 = (((2000000000000)/(math.sqrt(math.pow(rocket.xcor()-moon2.xcor(),2) + math.pow(rocket.ycor()-moon2.ycor(),2))*2)**2)*(6.67408*(10**-11)))
    angle5 = math.atan2(rocket.ycor()-planet1.ycor(),rocket.xcor()-planet1.xcor())
    angle6 = math.atan2(rocket.ycor()-moon.ycor(),rocket.xcor()-moon.xcor())
    angle7 = math.atan2(rocket.ycor()-moon2.ycor(),rocket.xcor()-moon2.xcor())
    accel_x5 = gravity5*math.cos(angle5)*-1  
    accel_y5 = gravity5*math.sin(angle5)*-1  
    accel_x6 = gravity6*math.cos(angle6)*-1 
    accel_y6 = gravity6*math.sin(angle6)*-1
    accel_x7 = gravity7*math.cos(angle7)*-1 
    accel_y7 = gravity7*math.sin(angle7)*-1
    vx5 += accel_x5 + accel_x6
    vy5 += accel_y5 + accel_y6
    vx6 += accel_x7
    vy6 += accel_y7
    gravity8 = (((10000000000000)/(moon2.distance(planet1)*2)**2)*(6.67408*(10**-11)))         
    gravity9 = (((10000000000000)/(moon2.distance(moon)*2)**2)*(6.67408*(10**-11)))     
    angle8 = math.atan2(moon2.ycor()-planet1.ycor(),moon2.xcor()-planet1.xcor())
    angle9 = math.atan2(moon2.ycor()-moon.ycor(),moon2.xcor()-moon.xcor())
    accel_x8 = gravity8*math.cos(angle8)*-1  
    accel_y8 = gravity8*math.sin(angle8)*-1  
    accel_x9 = gravity9*math.cos(angle9)*-1 
    accel_y9 = gravity9*math.sin(angle9)*-1
    vx8 += accel_x8+accel_x9
    vy8 += accel_y8+accel_y9
    while moon.distance(planet1) <= 20:
      turtle.done()
      sys.exit()
    while rocket.distance(planet1) <= 20: 
      vx5 = 0
      vy5 = 0
      turtle.bye()
      sys.exit()
    while rocket.distance(moon) <= 20:
      vx5 = 0
      vy5 = 0
      turtle.bye()
      sys.exit()
    while rocket.distance(moon2) <= 5:
      vx5 = 0
      vy5 = 0
      turtle.bye()
      sys.exit()
    while planet1.distance(moon2) <= 20:
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
    y5 += vy5 + vym + vy6
    x5 += vx5 + vxm + vx6
    rocket.goto(x5,y5)
    y8 += vy8
    x8 += vx8
    moon2.goto(x8,y8)
    
def keys():
  turtle.listen()
  turtle.onkey(rightfine,'d')
  turtle.onkey(leftfine,'a')
  turtle.onkey(upfine,'w')
  turtle.onkey(downfine,'s')
  turtle.onkey(right,'Right')
  turtle.onkey(left,'Left')
  turtle.onkey(up,'Up')
  turtle.onkey(down,'Down')
  turtle.onkey(leave,'x')

def leave():
  turtle.bye()
  sys.exit()


def rightfine():
  global x5
  global vxm
  vxm += 0.1
  x5 += vxm 
def upfine():
  global y5
  global vym
  vym += 0.1 
  y5 += vym
def downfine():
  global y5
  global vym
  vym -= 0.1  
  y5 += vym
def leftfine():
  global x5
  global vxm
  vxm -= 0.1
  x5 += vxm
def right():
  global x5
  global vxm
  vxm += 0.4
  x5 += vxm 
def up():
  global y5
  global vym
  vym += 0.4 
  y5 += vym
def down():
  global y5
  global vym
  vym -= 0.4 
  y5 += vym
def left():
  global x5
  global vxm
  vxm -= 0.4
  x5 += vxm


keys() 
gravity()  
 
  
  
