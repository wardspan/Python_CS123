# Import required module
import turtle

# Create turtle object
t = turtle.Turtle()

# Create a screen
screen =turtle.Screen()

# Set background color
screen.bgcolor("sky blue")



# Function to draw body of snowman
def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor (color)
    t.goto (x, y)
    t.pendown()
    t.begin_fill()
    t.circle (radius)
    t.end_fill()

# Drawing snowman body
draw_circle ("#ffffff", 30, 0, -40)
draw_circle ("#ffffff", 40, 0, -120)
draw_circle ("#ffffff", 50, 0, -220)

# Drawing left eye
draw_circle ("#ffffff", 2, -10, -10)

# Drawing right eye
draw_circle ("#ffffff", 2, 10, -10)

# Drawing nose
draw_circle ("#FF6600", 3, 0, -15)

# Drawing buttons on
draw_circle ("#ffffff", 2, 0, -55)
draw_circle ("#ffffff", 2, 0, -65)
draw_circle ("#ffffff", 2, 0, -75)



# Function to draw arms
def create_line(x, y, length, angle):
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.forward(length)
    t.setheading(angle + 20)
    t.forward(20)
    t.penup()
    t.back(20)
    t.pendown()
    t.setheading(angle - 20)
    t.forward(20)
    t.penup()
    t.home()

# Drawing left arm
create_line(-27, -50, 50, 160)

# Drawing right arm
create_line(27, -50, 50, 20)



# Drawing hat
t.penup()
t.goto (-35, 8)
t.color ("black")
t.pensize (6)
t.pendown()
t.goto (35, 8)

t.goto (30, 8)
t.fillcolor ("black")
t.begin_fill()
t.left (90)
t.forward (45)
t.left (90)
t.forward (60)
t.left (90)
t.forward (45)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()