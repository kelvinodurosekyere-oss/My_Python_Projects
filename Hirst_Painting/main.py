from turtle import Turtle,Screen
import random
screen = Screen() 

dif_shapes = [(10,3),(10,4),(10,5),(10,6)]
color_palet = [(236, 234, 231), (235, 232, 233), (229, 231, 235), (181, 149, 99), (226, 233, 228), (150, 100, 46), (175, 151, 30), (86, 31, 24), (15, 55, 69), (35, 100, 119)]
#setting background 
screen.colormode(255)
columns = 13
rows = 10
kev = Turtle()
kev.penup()
kev.speed(0)
start_x = -300
start_y = -250
spacing = 50

for column in range(columns):
    row_order = range(rows) if column % 2 == 0 else range(rows - 1, -1, -1)

    for row in row_order:
        kev.goto(start_x + column * spacing, start_y + row * spacing)
        radius, steps = random.choice(dif_shapes)
        kev.color(random.choice(color_palet))
        kev.setheading(0)
        kev.pendown()
        kev.begin_fill()
        kev.circle(radius, steps=steps)
        kev.end_fill()
        kev.penup()









screen.exitonclick













screen.exitonclick()









