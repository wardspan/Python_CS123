#Import turtle module 
import turtle


def NestedSquare(tDocsTurtle, side, delta):
    if side < delta: 
        return 
 
    #tDocsTurtle.penup()
    tDocsTurtle.goto(-(side-delta)/2, -(side-delta)/2)
    tDocsTurtle.pendown()
 
    for _ in range(4):
        tDocsTurtle.forward(side)
        tDocsTurtle.left(90) 

    # Recursive call to draw inner square
    NestedSquare(tDocsTurtle, side-delta, delta)
 

def main():
 WindowTurtleScreen=turtle.Screen()
 tDocsTurtle = turtle.Turtle()
 WindowTurtleScreen.title("Nested Squares")
 tDocsTurtle.penup()
 tDocsTurtle.goto(0, 0)
 tDocsTurtle.pendown()
 NestedSquare(tDocsTurtle,600,60) 
 WindowTurtleScreen.exitonclick()
 

main()