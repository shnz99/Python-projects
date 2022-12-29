from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.res_position()
        self.shape("turtle")
        self.seth(90)
        
    def up(self):
        self.fd(MOVE_DISTANCE)

    def res_position(self):
        self.goto(STARTING_POSITION)