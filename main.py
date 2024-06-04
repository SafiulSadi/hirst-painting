# import colorgram.py
# colors = colorgram.extract('')
import random
import turtle as t
t.colormode(255)
color_list = [(202,164,109), (150,75,49), (223,201,135), (52, 93, 124), (14,70,20),(30,68,100),(107,127,153),(174,94,97)]

tim = t.Turtle()
def move_dot():
    tim.penup()
    tim.forward(50)
    tim.dot(20, random.choice(color_list))

def line_dot():
    for _ in range(10):
        move_dot()

def moveup():
    tim.right(180)
    tim.forward(500)
    tim.right(180)
    tim.left(90)
    tim.forward(50)
    tim.right(90)
tim.hideturtle()

tim.speed(0)
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
for _ in range(10):
    line_dot()
    moveup()
screen = t.Screen()
screen.exitonclick()