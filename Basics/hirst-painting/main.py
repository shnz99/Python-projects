import turtle as t
import random as r
from colors import colors_dir

# 10 col, 10 row, size 20 distance between 50, random colors
t.colormode(255)
t.pensize = 20
tim = t.Turtle()
tim.speed(0)
tim.pu()
tim.hideturtle()

col = -250

for _ in range(10):
    col += 50
    tim.setposition(-240, col)
    for _ in range(10):
        tim.dot(20, r.choice(colors_dir))
        tim.fd(50)

screen = t.Screen()
screen.exitonclick()
