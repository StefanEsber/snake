import turtle
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20 , "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.sety(255)
        self.color("white")
        self.write(f"score: {self.score} ", False, align=ALIGNMENT, font=FONT)
        self.color("white")

    def snake_ate_food(self):
        self.score += 1
        self.clear()
        self.write(f"score : {self.score} ", False, align="center", font=("Arial", 20, "normal"))
