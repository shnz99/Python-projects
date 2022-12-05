from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.current_level = 1
        self.penup()
        self.ht()
        self.color("black")
        
    def write_level(self):
        self.clear()
        self.goto(-280,260)
        self.write(f"Level: {self.current_level}", align="left", font=FONT)

    def level_up(self):
        self.current_level+=1
        self.write_level()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=FONT)