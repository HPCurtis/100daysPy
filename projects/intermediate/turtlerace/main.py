# Programme to run a turtle race between me and my brothers
import turtle
import random
from utility import check_guess, move_to_side, move_forward

# These competitors are the names of my brothers
compeititors = ["harrison", "brandon", "fraser", "ashley"]

# Generate screen to present turtles on
screen = turtle.Screen()

# call chekc guess to get users guess who the winner will be
guess = check_guess(compeititors, screen)


# Get so works with and eight and width size of screen
width = screen.window_width()
height = screen.window_height()


# Set up the turtle racers
harrison = turtle.Turtle()
brandon = turtle.Turtle()
fraser = turtle.Turtle()
ashley = turtle.Turtle()

# Generate dictonary of the turtles
turtle_dict = {
    "harrison": harrison,
    "brandon": brandon,
    "fraser": fraser,
    "ashley": ashley
}

# give turtle a y-coord
y_coords = {
    "harrison": 0,
    "brandon": 30,
    "fraser": -30,
    "ashley": -60
}

# Set all to turtle as turle shape and with their colour
harrison.shape("turtle")
harrison.color("red")
brandon.shape("turtle")
brandon.color("green")
fraser.shape("turtle")
fraser.color("blue")
ashley.shape("turtle")
ashley.color("pink")

# Move all turtle to left edge of the screen 
for key in turtle_dict:
    move_to_side(turtle_dict[key], width, y_coords[key])


# Output the result of the race.
print(move_forward(turtle_dict, width, guess))

# Set so scrren will close upon click.
screen.exitonclick()