import turtle as t
import random

SIZEOFAREA = 260


class Food(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        random_x = random.randint(-SIZEOFAREA, SIZEOFAREA)
        random_y = random.randint(-SIZEOFAREA, SIZEOFAREA)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-SIZEOFAREA, SIZEOFAREA)
        random_y = random.randint(-SIZEOFAREA, SIZEOFAREA)
        self.goto(random_x, random_y)
