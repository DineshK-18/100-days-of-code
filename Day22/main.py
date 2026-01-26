import time
from turtle import Screen
from paddle import  Paddle
from ball import Ball
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.onkey(r_paddle.up, key='Up')
screen.onkey(r_paddle.down, key='Down')
screen.onkey(l_paddle.up, key='w')
screen.onkey(l_paddle.down, key='s')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

# Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# Detect collision with paddles.
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed()

# Detect the ball bounds.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()






screen.exitonclick()

