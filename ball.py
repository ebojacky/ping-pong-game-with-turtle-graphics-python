import random
from turtle import Turtle
import time

ONE_STEP = 20
DEFAULT_SPEED_SECS = 0.1
MAX_SPEED_SEC = 0.025
SPEED_INCREASE_FACTOR = 0.5
WAIT_FOR_NEW_BALL = 0.5


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.speed("fastest")
        self.penup()

        self.x_boundary = self.getscreen().window_width() / 2
        self.y_boundary = self.getscreen().window_height() / 2
        self.moving_speed = DEFAULT_SPEED_SECS

        self.reset_ball()

    def reset_ball(self, side="right"):
        self.moving_speed = DEFAULT_SPEED_SECS
        self.goto(0, 0)
        self.set_angle_randomly(side)
        time.sleep(WAIT_FOR_NEW_BALL)

    def set_angle_randomly(self, side):
        if side == "right":
            ball_angles = [15, 30, 45, 60, 300, 315, 330, 345]
        elif side == "left":
            ball_angles = [120, 135, 150, 165, 195, 210, 225, 240]
        self.setheading(random.choice(ball_angles))

    def move(self):
        self.forward(ONE_STEP)

    def bounce_off_wall(self):
        new_angle = abs(self.heading() - 360)
        self.setheading(new_angle)

    def bounce_off_paddle(self, side):
        self.set_angle_randomly(side)

    def increase_speed(self):
        if self.moving_speed > MAX_SPEED_SEC:
            self.moving_speed *= SPEED_INCREASE_FACTOR

