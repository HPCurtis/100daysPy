import turtle


t = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    t.forward(10)

def move_backwards():
    t.backward(10)

def move_left():
    new_heading = t.heading() + 10
    t.setheading(new_heading)

def move_right():
    new_heading = t.heading() - 10
    t.setheading(new_heading)

def clear_screen():
    t.clear()
    t.penup()
    t.home()


screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "a", fun=move_left)
screen.onkey(key = "d", fun=move_right)
screen.onkey(key = "s", fun=move_backwards)
screen.onkey(key = "c", fun=clear_screen)
screen.listen()
screen.exitonclick()