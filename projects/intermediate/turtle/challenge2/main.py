from turtle import Turtle, done

t = Turtle()

for _ in range(10):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

done()