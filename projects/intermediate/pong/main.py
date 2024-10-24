from turtle import Screen, Turtle

# Set up the porjects screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height = 600)
screen.title("Pong")

paddle = Turtle()

paddle.penup()
paddle.goto(350, 0)

paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("white")


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

screen.exitonclick()