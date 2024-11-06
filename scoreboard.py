from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-235,250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier",24, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Courier", 24, "normal"))