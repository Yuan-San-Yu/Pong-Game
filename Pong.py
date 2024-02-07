# Pong Game
# Author: Yuan San Yu

import turtle
import winsound

w = turtle.Screen() # create a window
w.title("Pong by Yuan San Yu")
w.bgcolor('black')
w.setup(width=800, height=600)
w.tracer(0)

# Player 1 (left)
p1 = turtle.Turtle()
p1.speed(0) # speed of animation
p1.shape("square")
p1.color("red")
p1.shapesize(stretch_wid=5, stretch_len=1)
p1.penup()
p1.goto(-350, 0) # left side of window

# Player 2 (right)
p2 = turtle.Turtle()
p2.speed(0) 
p2.shape("square")
p2.color("blue")
p2.shapesize(stretch_wid=5, stretch_len=1)
p2.penup()
p2.goto(350, 0) 

# Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0) 
ball.dx = 0.1 # moves 2 pixels at a time
ball.dy = -0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0     Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Score
s1 = 0
s2 = 0

# Functions


#Sound
def sound():
    winsound.PlaySound("Bonk Sound Effect.mp3", winsound.SND_ASYNC)

# Player 1 Functions
def p1_up():
    y = p1.ycor()
    y += 20
    p1.sety(y)

def p1_down():
    y = p1.ycor()
    y -= 20
    p1.sety(y)

# Player 2 Functions
def p2_up():
    y = p2.ycor()
    y += 20
    p2.sety(y)

def p2_down():
    y = p2.ycor()
    y -= 20
    p2.sety(y)

# Keyboard Bindings
w.listen()
w.onkeypress(p1_up, 'w')
w.onkeypress(p1_down, 's')

w.onkeypress(p2_up, 'Up')
w.onkeypress(p2_down, 'Down')

# Main Game Loop
while True:
    w.update() # updates screen every time loop runs

    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    # top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # reverses direction
        sound()

    # bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 
        sound()

    # right border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = 0.1
        sound()
        s1 += 1 # player 1 scores
        pen.clear() # clear old score
        pen.write("Player A: {}  Player B: {}".format(s1, s2), align="center", font=("Courier", 24, "normal"))

    # left border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = -0.1
        sound()
        s2 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(s1, s2), align="center", font=("Courier", 24, "normal"))


    # Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < p2.ycor() + 40 and ball.ycor() > p2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1.3 # speed up ball after every hit
        sound()
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < p1.ycor() + 40 and ball.ycor() > p1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1.3
        sound()
