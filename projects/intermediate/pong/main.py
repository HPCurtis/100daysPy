from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Global varaibles 
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
# This value must be set to SCREEN_HEIGHT - ballsize (20 pixels)
BOUNCE_LIMIT = 280

# Set up the projects screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width= SCREEN_WIDTH, height = SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))
ball = Ball((0,0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(screen.bye, "Escape")

game_is_on = True
while game_is_on:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()
    
    # Detect collisions with top bottom walls
    if ball.ycor() > BOUNCE_LIMIT or ball.ycor() < -BOUNCE_LIMIT:
        ball.bounce_y()
    
    # Detect colliosn with paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Specify R paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.r_point()

    # Specify R paddle misses
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.l_point() 

