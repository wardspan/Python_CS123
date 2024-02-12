import turtle 
polygon = turtle.Turtle()
 
num_sides = 5
side_length = 50
angle = 360.0 / num_sides

polygon.fillcolor("blue")
polygon.begin_fill()

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
     
polygon.hideturtle()
polygon.end_fill()
turtle.done()
