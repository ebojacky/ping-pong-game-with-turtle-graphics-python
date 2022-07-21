from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time

SCREEN_NAME = "PONG GAME"
WIDTH = 800
HEIGHT = 400
BACKCOLOR = "black"
PADDLE_MARGIN = 20
COLLISION_MARGIN_WALL = 20
COLLISION_MARGIN_PADDLE = 50
BALL_PADDLE_MIDDLE_DISTANCE_MARGIN = 20
SCOREBOARD_POSITION_LEFT = (-200, 100)
SCOREBOARD_POSITION_RIGHT = (200, 100)
WINNER_BOARD_POSITION = (0, 100)
LEFT_PADDLE_COLOR = "red"
RIGHT_PADDLE_COLOR = "green"

WINNING_SCORE = 10


def play_game():
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title(SCREEN_NAME)
    screen.bgcolor(BACKCOLOR)
    screen.tracer(0)

    left_paddle = Paddle("left", LEFT_PADDLE_COLOR)
    right_paddle = Paddle("right", RIGHT_PADDLE_COLOR)
    ball = Ball()
    left_score = ScoreBoard(SCOREBOARD_POSITION_LEFT[0], SCOREBOARD_POSITION_LEFT[1])
    right_score = ScoreBoard(SCOREBOARD_POSITION_RIGHT[0], SCOREBOARD_POSITION_RIGHT[1])

    winner_scoreboard = ScoreBoard(WINNER_BOARD_POSITION[0], WINNER_BOARD_POSITION[1], False)
    screen.listen()
    screen.onkey(left_paddle.up, "a")
    screen.onkey(left_paddle.down, "z")
    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")

    game_on = True
    while game_on:
        time.sleep(ball.moving_speed)
        screen.update()
        ball.move()

        # detect collision with walls
        if abs(ball.ycor()) >= ball.y_boundary - COLLISION_MARGIN_WALL:
            ball.bounce_off_wall()

        # detect collision with paddles
        if ball.distance(right_paddle) <= COLLISION_MARGIN_PADDLE \
                and abs(ball.xcor()) >= abs(right_paddle.xcor()) - BALL_PADDLE_MIDDLE_DISTANCE_MARGIN:
            ball.bounce_off_paddle("left")
            ball.increase_speed()

        if ball.distance(left_paddle) <= COLLISION_MARGIN_PADDLE \
                and abs(ball.xcor()) >= abs(left_paddle.xcor()) - BALL_PADDLE_MIDDLE_DISTANCE_MARGIN:
            ball.bounce_off_paddle("right")
            ball.increase_speed()

        # detect a miss
        if abs(ball.xcor()) >= ball.x_boundary:
            if ball.xcor() < 0:
                ball.reset_ball("right")
                right_score.update_score()
            else:
                ball.reset_ball("left")
                left_score.update_score()

        # check for winner
        if right_score.score >= WINNING_SCORE:
            winner_scoreboard.declare_winner(RIGHT_PADDLE_COLOR)
            game_on = False

        if left_score.score >= WINNING_SCORE:
            winner_scoreboard.declare_winner(LEFT_PADDLE_COLOR)
            game_on = False

    play_again = screen.textinput("Play Again", "Do you want to play again ? (Y or N) : ")
    if play_again.upper() == "Y":
        screen.clear()
        play_game()

    screen.exitonclick()


play_game()
