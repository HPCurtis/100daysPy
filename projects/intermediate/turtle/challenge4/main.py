from turtle import Turtle, done
import random


def main():
    random_walk()

def random_walk():
    # create turtler object.
    t = Turtle()
    # Set the speed to it maximum.
    t.speed(0)
    # Set the width.
    t.width(5)
    for i in range(500):
        t.pencolor(random_colour())
        t.forward(10)
        t.setheading(random_compass())
    done()

def random_compass():
    headings = [0, 90,180, 270]
    return random.choice(headings)

def random_colour():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    # Convert RGB to hex color code
    color_code = "#{:02x}{:02x}{:02x}".format(red, green, blue)

    return color_code

if __name__ == "__main__":
    main()