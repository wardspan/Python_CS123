# Write a turtle graphics program that uses nested loops to draw 100 squares
# in a row. Each square will be drawn in a different color. The colors will
# cycle through a set of six pre-defined colors.

import turtle

# Define the colors
colors = ["red", "orange", "pink", "green", "blue", "purple"]

# Set up the turtle
turtle.speed(0)
turtle.penup()
turtle.goto(200, -200)
turtle.pendown()

# Draw the squares
size = 20
for i in range(100):
    turtle.color(colors[i % 6])
    for _ in range(4):
        turtle.backward(size)
        turtle.right(90)
    size += 5
    
turtle.Screen().exitonclick()
