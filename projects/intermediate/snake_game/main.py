from turtle import Turtle, Screen
import time
from snake import Snake
# Set screen object and important values.
# Specify script constants
WIDTH = 600
HEIGHT = 600
SLEEP_TIME = .1

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Generte object of the snake class.
snake = Snake()
# Specify that from here in the code keystrokes are being listened for.
screen.listen()

# Create key bindings
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

on = True
while on:
    screen.update()
    time.sleep(SLEEP_TIME)

    snake.move()

screen.exitonclick()