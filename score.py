import turtle
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, x, y, write_score=True):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(x, y)

        self.score = 0
        if write_score:
            self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.score}\n", font=('Arial', 16, 'normal'))

    def declare_winner(self, color):
        self.clear()
        self.write(f"GAME OVER\n{color.upper()} WINS", font=('Arial', 16, 'normal'), align='center')

    def update_score(self):
        self.score += 1
        self.write_score()
