from turtle import Turtle

WIDTH_FACTOR = 5
LEN_FACTOR = 1
MARGIN = 40
ONE_STEP = 50


class Paddle(Turtle):
    def __init__(self, side, color):
        super().__init__()
        self.shapesize(stretch_wid=WIDTH_FACTOR, stretch_len=LEN_FACTOR)
        self.shape("square")
        self.color(color)
        self.speed("fastest")
        self.penup()

        self.side_of_screen = side
        self.x_boundary = self.getscreen().window_width() / 2
        self.y_boundary = self.getscreen().window_height() / 2

        self.goto_init_position()

    def goto_init_position(self):
        if self.side_of_screen == "left":
            self.goto(-(self.x_boundary - MARGIN), 0)
        elif self.side_of_screen == "right":
            self.goto((self.x_boundary - MARGIN), 0)

    def up(self):
        if self.ycor() < self.y_boundary:
            self.goto(self.xcor(), self.ycor() + ONE_STEP)

    def down(self):
        if self.ycor() > -self.y_boundary:
            self.goto(self.xcor(), self.ycor() - ONE_STEP)
