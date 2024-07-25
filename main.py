# 1. Create the screen
# 2. Create and move the paddle
# 3. Create another paddle for second player
# 4. create the ball and make it move
# 5. Detect collision with the wall and bounce
# 6. Detect collision with the wall
# 7. Detect when the paddle misses
# 8. Keep score
import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score

left_score = Score()
# left_score.penup()
# left_score.hideturtle()
right_score = Score()
# right_score.penup()
# right_score.hideturtle()
screen = Screen()
screen.tracer(0)

screen.title("PONG GAME")
screen.setup(width=800, height=600)
screen.bgcolor('orange')
right_score.goto(100, 250)
right_score.write(f"{right_score.score}", move=False, align='center', font=('Arial', 50, 'normal'))
left_score.goto(-100, 250)
left_score.write(f"{left_score.score}", move=False, align='center', font=('Arial', 50, 'normal'))

paddle_left = Paddle(-350, 0)
paddle_right = Paddle(350, 0)
ball = Ball()
screen.listen()
screen.onkey(key='w', fun=paddle_left.up)
screen.onkey(key='s', fun=paddle_left.down)

screen.onkey(key='Up', fun=paddle_right.up)
screen.onkey(key='Down', fun=paddle_right.down)
is_game_on = True
while is_game_on:
    time.sleep(ball.speed_ball)
    screen.update()
    ball.move()
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.wall_bounce()
    # Detect Collision With paddle
    if ball.xcor() == 320 and ball.distance(paddle_right) <= 70:
        ball.paddle_bounce()
    elif ball.xcor() == -320 and ball.distance(paddle_left) <= 70:
        ball.paddle_bounce()
    # miss paddle
    elif ball.xcor() > 320:
        left_score.change_score()
        left_score.clear()
        left_score.write(f"{left_score.score}", move=False, align='center', font=('Arial', 50, 'normal'))
        ball.reset_position()
        ball.x_move = -10
        ball.y_move = -10
    elif ball.xcor() < -320:
        right_score.change_score()
        right_score.clear()
        right_score.write(f"{right_score.score}", move=False, align='center', font=('Arial', 50, 'normal'))
        ball.reset_position()
        ball.x_move = 10
        ball.y_move = 10
screen.exitonclick()
