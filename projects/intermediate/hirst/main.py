###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
'''
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_c  =(r,g,b)
    rgb_colors.append(new_c)


# Create threshold close to white
threshold = 255

# Filter out tuples close to white
filtered_rgb_colors = [rgb for rgb in rgb_colors if max(rgb) < threshold]
print(rgb_colors)
'''

import turtle
import random
colours = [ 
            (202, 164, 109), (238, 240, 245), (150, 75, 49), 
            (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), 
            (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), 
            (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), 
            (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), 
            (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153),
            (174, 94, 97), (176, 192, 209)
            ]

dot_size = 25


t = turtle.Turtle()
screen = turtle.Screen()
t.speed(0)
# change color mode to tack tuple
screen.colormode(255)
dots_per_row = 5
n_rows = 7

for i in range(n_rows):
    for j in range(dots_per_row):

        t.pendown()
        # Code to draw dot of random color
        t.pencolor(random.choice(colours))
        t.dot(dot_size)
        t.penup()
        if j < dots_per_row - 1:
            t.forward(40)
        if j == dots_per_row - 1:
            t.left(180)
            t.forward((dots_per_row - 1) * 40)
            t.right(90)
            t.forward(40)
            t.right(90)

# Remove turtle of screen for viewing experience.
t.hideturtle()

# Keep the window open until user closes it
turtle.mainloop()