# Programme to run a turtle race between me and my brothers
import turtle
import random
from utility import check_guess, move_to_side, move_forward

compeititors = ["harrison", "brandon", "fraser", "ashley"]

screen = turtle.Screen()
#screen.setup(5000,400)

guess = check_guess(compeititors, screen)

# Get so works with and eight and width size of screen
width = screen.window_width()
height = screen.window_height()


# set up the turtle racers
harrison = turtle.Turtle()
brandon = turtle.Turtle()
fraser = turtle.Turtle()
ashley = turtle.Turtle()

turtle_dict = {
    "harrison": harrison,
    "brandon": brandon,
    "fraser": fraser,
    "ashley": ashley
}
y_coords = {
    "harrison": 0,
    "brandon": 30,
    "fraser": -30,
    "ashley": -60
}

# Set all to turtle iamges
harrison.shape("turtle")
harrison.color("red")
brandon.shape("turtle")
brandon.color("green")
fraser.shape("turtle")
fraser.color("blue")
ashley.shape("turtle")
ashley.color("pink")

 
for key in turtle_dict:
    move_to_side(turtle_dict[key], width, y_coords[key])

print(move_forward(turtle_dict, width, guess))

screen.exitonclick()