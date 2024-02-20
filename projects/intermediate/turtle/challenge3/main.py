# Refactor code in to funtion and with main() strcuture
from turtle import Turtle, done
from random import choice
t = Turtle()
angles = []
colours = ['black', 'blue', 'red', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'cyan']

for i in range(3, 11):
    angles.append(360/i)

sides = 3

for angle in angles:
    counter = 0
    t.color(choice(colours))
    while True:
        t.forward(100)  
        t.right(angle)
        counter += 1
        if counter >= sides:
            break
    sides += 1

done()