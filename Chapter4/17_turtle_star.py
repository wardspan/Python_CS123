# Use a loop with the turtle graphics library to draw a star.
import turtle

# Create a turtle object
star = turtle.Turtle()

# Set the speed of the turtle
star.speed(5)

# Move the turtle to the starting position
star.penup()
star.goto(-100, 0)
star.pendown()

# Draw the star
for _ in range(8):
    star.forward(200)
    star.right(135)

# Close the turtle graphics window
turtle.Screen().exitonclick()