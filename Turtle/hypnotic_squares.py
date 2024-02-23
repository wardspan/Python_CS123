import turtle

# Draw a square
NUM_SQUARES = 100
SIDE_LENGTH = 50
ANGLE = 90
ANIMATION_SPEED = 0

turtle.speed(ANIMATION_SPEED)

# Move the turtle to its initial position.
turtle.hideturtle()
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

for x in range(NUM_SQUARES):
    turtle.forward(SIDE_LENGTH)
    turtle.left(ANGLE)
    SIDE_LENGTH += 10
    
turtle.done()
# End of program