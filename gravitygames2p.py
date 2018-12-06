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
moon.shapesize(1)
moon.shape('circle')
moon.penup()
rocket = turtle.Turtle()
rocket.penup()
rocket.shapesize(0.5)
rocket.color('blue')
rocket2 = turtle.Turtle()
rocket2.penup()
rocket2.shapesize(0.5)
rocket2.color('red')
bullet =  turtle.Turtle()
bullet.penup()
bullet.shapesize(0.3)
bullet.color('yellow')
bullet2 =  turtle.Turtle()
bullet2.penup()
bullet2.shapesize(0.3)
bullet2.color('yellow')
turtle.tracer(2)
moon2 = turtle.Turtle()
moon2.color('cyan')
moon2.shapesize(0.75)
moon2.shape('circle')
moon2.penup()
status = 'ready'
status2 = 'ready'

vx1 = 0.65
vy1 = 0
x1 = 0
y1 = 400 
moon.goto(x1,y1)
moon.penup()
moon.speed(0)
vx6 = 0
vy6 = 0
vx5 = 2
vy5 = 0
x5 = 0
y5 = 40
rocket.goto(x5,y5) 
rocket.speed(0)
vx11 = 0
vy11 = 0
vx10 = -2
vy10 = 0
x10 = 0
y10 = -40
rocket2.goto(x10,y10) 
rocket2.speed(0)
vx16 = 0
vy16 = 0
vx15 = 0
vy15 = 0
x15 = 999
y15 = 999
bullet.goto(x15,y15) 
bullet.speed(0)
vx21 = 0
vy21 = 0
vx20 = 0
vy20 = 0
x20 = 999
y20 = 999
bullet2.goto(x20,y20) 
bullet2.speed(0)
vx8 = 0.8
vy8 = 0
x8 = 0 
y8 = 250
moon2.goto(x8,y8) 
moon2.speed(0)
vx3 = -0.02
vy3 = -0.006
x3 = 0
y3 = 0 
planet1.speed(0)
planet1.penup()
planet1.goto(x3,y3)
vxm = 0
vym = 0
vxm2 = 0
vym2 = 0
accel_x23 = 0 
accel_y23 = 0
accel_x18 = 0 
accel_y18 = 0
def gravity():
  global x1
  global y1
  global x3
  global y3
  global x5
  global y5
  global x8
  global y8
  global x10
  global y10
  global x15
  global y15
  global x20
  global y20
  global vx1
  global vy1
  global vx3
  global vy3
  global vx5
  global vy5
  global vx6
  global vy6 
  global vx10
  global vy10
  global vx11
  global vy11
  global vx16
  global vy16  
  global vx15
  global vy15
  global vx16
  global vy16 
  global vx20
  global vy20
  global vx21
  global vy21 
  global vx8
  global vy8
  global vxm
  global vym
  global vxm2
  global vym2
  global status
  global status2
  global accel_x18
  global accel_y18
  global accel_x23
  global accel_y23
  while True:
    gravity1 = (((10000000000000)/(moon.distance(planet1)*2)**2)*(6.67408*(10**-11)))    
    gravity2 = (((20000000000)/(moon.distance(moon2)*2)**2)*(6.67408*(10**-11)))    
    angle1 = math.atan2(moon.ycor()-planet1.ycor(),moon.xcor()-planet1.xcor())
    angle2 = math.atan2(moon.ycor()-rocket.ycor(),moon.xcor()-rocket.xcor())
    accel_x1 = gravity1*math.cos(angle1)*-1 
    accel_y1 = gravity1*math.sin(angle1)*-1
    accel_x2 = gravity2*math.cos(angle2)*-1 
    accel_y2 = gravity2*math.sin(angle2)*-1   
    vx1 += accel_x1+accel_x2
    vy1 += accel_y1+accel_y2
    gravity3 = (((300000000000)/(planet1.distance(moon)*2)**2)*(6.67408*(10**-11)))     
    gravity4 = (((20000000000)/(planet1.distance(moon2)*2)**2)*(6.67408*(10**-11)))     
    angle3 = math.atan2(planet1.ycor()-moon.ycor(),planet1.xcor()-moon.xcor())
    angle4 = math.atan2(planet1.ycor()-rocket.ycor(),planet1.xcor()-rocket.xcor())
    accel_x3 = gravity3*math.cos(angle3)*-1 
    accel_y3 = gravity3*math.sin(angle3)*-1
    accel_x4 = gravity4*math.cos(angle4)*-1 
    accel_y4 = gravity4*math.sin(angle4)*-1   
    vx3 += accel_x3+accel_x4
    vy3 += accel_y3+accel_y4
    gravity5 = (((10000000000000)/(math.sqrt(math.pow(rocket.xcor()-planet1.xcor(),2) + math.pow(rocket.ycor()-planet1.ycor(),2))*2)**2)*(6.67408*(10**-11)))         
    gravity6 = (((3000000000000)/(math.sqrt(math.pow(rocket.xcor()-moon.xcor(),2) + math.pow(rocket.ycor()-moon.ycor(),2))*2)**2)*(6.67408*(10**-11)))     
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
    gravity10 = (((10000000000000)/(math.sqrt(math.pow(rocket2.xcor()-planet1.xcor(),2) + math.pow(rocket2.ycor()-planet1.ycor(),2))*2)**2)*(6.67408*(10**-11)))         
    gravity11 = (((3000000000000)/(math.sqrt(math.pow(rocket2.xcor()-moon.xcor(),2) + math.pow(rocket2.ycor()-moon.ycor(),2))*2)**2)*(6.67408*(10**-11)))     
    gravity12 = (((2000000000000)/(math.sqrt(math.pow(rocket2.xcor()-moon2.xcor(),2) + math.pow(rocket2.ycor()-moon2.ycor(),2))*2)**2)*(6.67408*(10**-11)))
    angle10 = math.atan2(rocket2.ycor()-planet1.ycor(),rocket2.xcor()-planet1.xcor())
    angle11 = math.atan2(rocket2.ycor()-moon.ycor(),rocket2.xcor()-moon.xcor())
    angle12 = math.atan2(rocket2.ycor()-moon2.ycor(),rocket2.xcor()-moon2.xcor())
    accel_x10 = gravity10*math.cos(angle10)*-1  
    accel_y10 = gravity10*math.sin(angle10)*-1  
    accel_x11 = gravity11*math.cos(angle11)*-1 
    accel_y11 = gravity11*math.sin(angle11)*-1
    accel_x12 = gravity12*math.cos(angle12)*-1 
    accel_y12 = gravity12*math.sin(angle12)*-1
    vx10 += accel_x10 + accel_x11
    vy10 += accel_y10 + accel_y11
    vx11 += accel_x12
    vy11 += accel_y12 
    gravity15 = (((10000000000000)/(math.sqrt(math.pow(bullet.xcor()-planet1.xcor(),2) + math.pow(bullet.ycor()-planet1.ycor(),2))*2)**2)*(6.67408*(10**-11)))         
    gravity16 = (((3000000000000)/(math.sqrt(math.pow(bullet.xcor()-moon.xcor(),2) + math.pow(bullet.ycor()-moon.ycor(),2))*2)**2)*(6.67408*(10**-11)))     
    gravity17 = (((2000000000000)/(math.sqrt(math.pow(bullet.xcor()-moon2.xcor(),2) + math.pow(bullet.ycor()-moon2.ycor(),2))*2)**2)*(6.67408*(10**-11)))
    angle15 = math.atan2(bullet.ycor()-planet1.ycor(),bullet.xcor()-planet1.xcor())
    angle16 = math.atan2(bullet.ycor()-moon.ycor(),bullet.xcor()-moon.xcor())
    angle17 = math.atan2(bullet.ycor()-moon2.ycor(),bullet.xcor()-moon2.xcor())
    angle18 = rocket.heading()
    accel_x15 = gravity15*math.cos(angle15)*-1  
    accel_y15 = gravity15*math.sin(angle15)*-1  
    accel_x16 = gravity16*math.cos(angle16)*-1 
    accel_y16 = gravity16*math.sin(angle16)*-1
    accel_x17 = gravity17*math.cos(angle17)*-1 
    accel_y17 = gravity17*math.sin(angle17)*-1
    vx15 += accel_x15 + accel_x16
    vy15 += accel_y15 + accel_y16
    vx16 += accel_x17 + accel_x18
    vy16 += accel_y17 + accel_y18
    gravity20 = (((10000000000000)/(math.sqrt(math.pow(bullet2.xcor()-planet1.xcor(),2) + math.pow(bullet2.ycor()-planet1.ycor(),2))*2)**2)*(6.67408*(10**-11)))         
    gravity21 = (((3000000000000)/(math.sqrt(math.pow(bullet2.xcor()-moon.xcor(),2) + math.pow(bullet2.ycor()-moon.ycor(),2))*2)**2)*(6.67408*(10**-11)))     
    gravity22 = (((2000000000000)/(math.sqrt(math.pow(bullet2.xcor()-moon2.xcor(),2) + math.pow(bullet2.ycor()-moon2.ycor(),2))*2)**2)*(6.67408*(10**-11)))
    angle20 = math.atan2(bullet2.ycor()-planet1.ycor(),bullet2.xcor()-planet1.xcor())
    angle21 = math.atan2(bullet2.ycor()-moon.ycor(),bullet2.xcor()-moon.xcor())
    angle22 = math.atan2(bullet2.ycor()-moon2.ycor(),bullet2.xcor()-moon2.xcor())
    angle23 = rocket2.heading()
    accel_x20 = gravity20*math.cos(angle20)*-1  
    accel_y20 = gravity20*math.sin(angle20)*-1  
    accel_x21 = gravity21*math.cos(angle21)*-1 
    accel_y21 = gravity21*math.sin(angle21)*-1
    accel_x22 = gravity22*math.cos(angle22)*-1 
    accel_y22 = gravity22*math.sin(angle22)*-1  
    vx20 += accel_x21 + accel_x20
    vy20 += accel_y21 + accel_y20
    vx21 += accel_x22 + accel_x23
    vy21 += accel_y22 + accel_y23
    gravity8 = (((10000000000000)/(moon2.distance(planet1)*2)**2)*(6.67408*(10**-11)))         
    gravity9 = (((30000000000)/(moon2.distance(moon)*2)**2)*(6.67408*(10**-11)))     
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
    while rocket.distance(moon) <= 10:
      vx5 = 0
      vy5 = 0
      turtle.bye()
      sys.exit()
    while rocket.distance(moon2) <= 5:
      vx5 = 0
      vy5 = 0
      turtle.bye()
      sys.exit()
    while rocket2.distance(planet1) <= 20: 
      vx5 = 0
      vy5 = 0
      turtle.bye()
      sys.exit()
    while rocket2.distance(moon) <= 10:
      vx5 = 0
      vy5 = 0
      turtle.bye()
      sys.exit()
    while rocket2.distance(moon2) <= 5:
      vx5 = 0
      vy5 = 0
      turtle.bye()
      sys.exit()
    while planet1.distance(moon2) <= 20:
      vx5 = 0
      vy5 = 0
      turtle.bye()
      sys.exit()
    while rocket.distance(bullet2) <= 3:
      print('Red wins!')
      turtle.bye()
      sys.exit()
    while rocket2.distance(bullet) <= 3:
      print('Blue wins!')
      turtle.bye()
      sys.exit()
    while bullet.distance(planet1) <= 20: 
      bullet.setpos(999,999)
      accel_x18 = 0 
      accel_y18 = 0
      vx16 = 0 
      vy16 = 0
      vx15 = 0
      vy15 = 0
      x15 = 999
      y15 = 999
    while bullet.distance(moon) <= 10:
      bullet.setpos(999,999)
      accel_x18 = 0 
      accel_y18 = 0
      vx16 = 0 
      vy16 = 0
      vx15 = 0
      vy15 = 0
      x15 = 999
      y15 = 999
    while bullet.distance(moon2) <= 5: 
      bullet.setpos(999,999)
      accel_x18 = 0 
      accel_y18 = 0
      vx16 = 0 
      vy16 = 0
      vx15 = 0
      vy15 = 0
      x15 = 999
      y15 = 999
    while bullet2.distance(planet1) <= 20: 
      bullet2.setpos(999,999)
      accel_x23 = 0 
      accel_y23 = 0
      vx21 = 0 
      vy21 = 0
      vx20 = 0 
      vy20 = 0
      x20 = 999
      y20 = 999
    while bullet2.distance(moon) <= 10:
      bullet2.setpos(999,999)
      accel_x23 = 0 
      accel_y23 = 0
      vx21 = 0 
      vy21 = 0
      vx20 = 0 
      vy20 = 0
      x20 = 999
      y20 = 999
    while bullet2.distance(moon2) <= 5:
      bullet2.setpos(999,999)
      accel_x23 = 0 
      accel_y23 = 0
      vx21 = 0 
      vy21 = 0
      vx20 = 0 
      vy20 = 0
      x20 = 999
      y20 = 999 
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
    y10 += vy10 + vym2 + vy11
    x10 += vx10 + vxm2 + vx11
    rocket2.goto(x10,y10)
    y15 += vy15 + vy16
    x15 += vx15 + vx16
    bullet.goto(x15,y15) 
    y20 += vy20 + vy21
    x20 += vx20 + vx21
    bullet2.goto(x20,y20)
    if status == 'firing':
      vx17 = 3*math.cos(rocket.heading())
      vy17 = 3*math.sin(rocket.heading())
      vx16 += accel_x17
      vy16 += accel_y17
      for times in range(0,1):
        x15 += vx17
        y15 += vy17
        bullet.goto(x15,y15)
      if bullet.xcor()>500 or bullet.xcor()<-500 or bullet.ycor()>500 or bullet.ycor()<-500:
        status = 'ready'
        bullet.setpos(999,999)
        accel_x18 = 0 
        accel_y18 = 0
        vx16 = 0 
        vy16 = 0
        vx15 = 0
        vy15 = 0
    elif status2 == 'firing':
      vx22 = 3*math.cos(rocket2.heading())
      vy22 = 3*math.sin(rocket2.heading())
      vx21 += accel_x21
      vy21 += accel_y21
      for times in range(0,1): 
        y20 += vy22
        x20 += vx22
        bullet2.goto(x20,y20)
      y20 += vy20 + vy21
      x20 += vx20 + vx21
      if bullet2.xcor()>500 or bullet2.xcor()<-500 or bullet2.ycor()>500 or bullet2.ycor()<-500:
        status2 = 'ready'
        bullet2.setpos(999,999)
        accel_x23 = 0 
        accel_y23 = 0
        vx21 = 0 
        vy21 = 0
        vx20 = 0 
        vy20 = 0
    y15 += vy15 + vy16
    x15 += vx15 + vx16
    bullet.goto(x15,y15)
    y20 += vy20 + vy21
    x20 += vx20 + vx21
    bullet2.goto(x20,y20)

def keys():
  turtle.listen()
  turtle.onkey(right2,'d')
  turtle.onkey(left2,'a')
  turtle.onkey(up2,'w')
  turtle.onkey(down2,'s')
  turtle.onkey(right,'Right')
  turtle.onkey(left,'Left')
  turtle.onkey(up,'Up')
  turtle.onkey(down,'Down')
  turtle.onkey(leave,'x')
  turtle.onkey(fire,'m')
  turtle.onkey(fire2,'f')
  turtle.onkey(rightturn,'n')
  turtle.onkey(leftturn,'b')
  turtle.onkey(rightturn2,'e')
  turtle.onkey(leftturn2,'q')
  
def rightturn():
  rocket.rt(20)
def leftturn():
  rocket.lt(20)
def rightturn2():
  rocket2.rt(20)
def leftturn2():
  rocket2.lt(20)
def leave():
  turtle.bye()
  sys.exit()

def fire():
  global status
  global x15
  global y15
  status = 'firing'
  x15 = rocket.xcor()
  y15 = rocket.ycor()
  bullet.setpos(x15,y15)



def fire2():
  global status2
  global x20
  global y20
  status2 = 'firing'
  x20 = rocket2.xcor()
  y20 = rocket2.ycor()
  bullet2.setpos(x20,y20)
  
    

def right2():
  global x5
  global vxm2
  vxm2 += 0.25
  x5 += vxm 
def up2():
  global y5
  global vym2
  vym2 += 0.25 
  y5 += vym
def down2():
  global y5
  global vym2
  vym2 -= 0.25  
  y5 += vym
def left2():
  global x5
  global vxm2
  vxm2 -= 0.25
  x5 += vxm
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
