import turtle
import random
import math
import sys
import time
wn = turtle.Screen()
wn.bgcolor('white')
wn.tracer(3)
points = 0

mypen = turtle.Turtle()
mypen.penup()
mypen.setpos(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
  mypen.forward(600)
  mypen.left(90)
mypen.hideturtle()



player = turtle.Turtle()
player.color('black')
player.penup()
player.speed(0)
player.shape('turtle')
speed = 3


def turnleft():
  player.left(45)

def turnright():
  player.right(45)

def increasespeed():
  global speed
  speed+=3

def brakes():
  global speed
  speed-=3

maxgoals = 6
goals = []

for count in range(maxgoals):
  goals.append(turtle.Turtle())

for goal in goals:
  goal.right(random.randint(0,360))
  goal.color('blue')
  goal.shape('circle')
  goal.penup()
  goal.speed(0)
  goal.setpos(random.randint(-300,300),random.randint(-300,300))
  speed2 = 0.75
  

maxspikes = 12
spikes = []


for count2 in range(maxspikes):
  spikes.append(turtle.Turtle())

for spike in spikes:
  spike.left(90)
  spike.color('red')
  spike.shape('triangle')
  spike.penup()
  spike.speed(0)
  spike.setpos(random.randint(-300,300),random.randint(-300,300))
  if -50 < spike.xcor() < 50 and -50 < spike.ycor() < 50:
    spike.setpos(random.randint(-300,300),random.randint(-300,300))
turtle.listen()
turtle.onkey(turnleft,'Left')
turtle.onkey(turnright,'Right')
turtle.onkey(increasespeed,'Up')
turtle.onkey(brakes,'Down')



while True:
  player.forward(speed)


  if player.xcor() > 300: 
    player.right(180)
    player.goto(298,player.ycor())
  if player.xcor() < -300:
    player.right(180)
    player.goto(-298,player.ycor())
  if player.ycor() > 300: 
    player.right(180)
    player.goto(player.xcor(),298)
  if player.ycor() < -300:
    player.right(180)
    player.goto(player.xcor(),-298)


 
  for goal in goals:
    d = math.sqrt(math.pow(player.xcor()-goal.xcor(),2) + math.pow(player.ycor()-goal.ycor(),2))
    if d<20:
      goal.hideturtle()
      goal.goto(random.randint(-300,300),random.randint(-300,300))
      goal.showturtle()
      points+=1
      goal.right(random.randint(0,360))
      scorestring = 'Score:%s' %points
      mypen.undo()
      mypen.penup()
      mypen.hideturtle()
      mypen.setposition(-290,310)
      mypen.write(scorestring, False, align='left', font=('Arial',14, 'normal'))

  
  for goal in goals:
    goal.forward(speed2)
    if goal.xcor() > 300: 
      goal.right(180)
      goal.goto(298,goal.ycor())
    if goal.xcor() < -300:
      goal.right(180)
      goal.goto(-298,goal.ycor())
    if goal.ycor() > 300: 
      goal.right(180)
      goal.goto(goal.xcor(),298)
    if goal.ycor() < -300:
      goal.right(180)
      goal.goto(goal.xcor(),-298)
      



  for spike in spikes:
    ded = math.sqrt(math.pow(player.xcor()-spike.xcor(),2) + math.pow(player.ycor()-spike.ycor(),2))
    while ded < 20.0:
      wn.clear()
      turtle.bye()
      if points>=20:   
        print('You Win.You got',points,'points')
      else:
        print('You Lost. You got',points,'points You need 20 points.')
      sys.exit()
