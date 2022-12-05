from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.y_heading = 0
        self.setpos(x=x_pos, y=y_pos)
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        self.y_heading += 20
        self.sety(self.y_heading)

    def down(self):
        self.y_heading -= 20
        self.sety(self.y_heading)
