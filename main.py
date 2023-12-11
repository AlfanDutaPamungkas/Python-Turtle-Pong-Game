from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

is_game_on = True
screen = Screen()
screen.title("Pong")
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(key = "Up", fun = r_paddle.go_up)
screen.onkey(key = "Down", fun = r_paddle.go_down)
screen.onkey(key = "w", fun = l_paddle.go_up)
screen.onkey(key = "s", fun = l_paddle.go_down)

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed /= 1.2
        
    if ball.xcor() > 380:
        ball.reset()
        score.increase_l_score()
        
    if ball.xcor() < -380:
        ball.reset()
        score.increase_r_score()

screen.exitonclick()