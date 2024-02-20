from turtle import Turtle, Screen
import random

def main():
    
    r = 50
    t = Turtle()
    gap_size = 10
    t.speed(0)
    for _ in range(int(360/gap_size)):
        t.pencolor(random_colour())
        t.circle(r)
        t.left(gap_size)

    screen = Screen()
    screen.exitonclick()

def random_colour():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    # Convert RGB to hex color code
    color_code = "#{:02x}{:02x}{:02x}".format(red, green, blue)
    return color_code

if __name__ == "__main__":
    main()