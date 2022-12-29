from turtle import Turtle
ALIGNEMENT = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_highscore()
        self.penup()
        self.ht()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False,
                   ALIGNEMENT, FONT)
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over.", False,
    #                ALIGNEMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
        
    def save_highscore(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.highscore}")
    
    def read_highscore(self):
        with open("data.txt") as file:
            self.highscore = int(file.read())