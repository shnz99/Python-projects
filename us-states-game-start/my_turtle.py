from turtle import Turtle

FONT = ['Arial', 8, 'normal']
image = 'blank_states_img.gif'

class WritingTurtle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.ht()
        
    def write_state(self, data, x, y):
        self.goto(x=x,y=y)
        self.write(f"{data}", False, "center", FONT)