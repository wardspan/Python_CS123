import turtle

def drawBase():
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.circle(100)

def drawMidSection():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.circle(80)

def drawArms():
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.forward(100)
    turtle.penup()
    turtle.goto(50, 50)
    turtle.pendown()
    turtle.forward(100)

def drawHead():
    turtle.penup()
    turtle.goto(0, 150)
    turtle.pendown()
    turtle.circle(40)

    turtle.penup()
    turtle.goto(-10, 180)
    turtle.pendown()
    turtle.dot(10)

    turtle.penup()
    turtle.goto(10, 180)
    turtle.pendown()
    turtle.dot(10)

    turtle.penup()
    turtle.goto(0, 170)
    turtle.pendown()
    turtle.circle(10, 180)

def drawHat():
    turtle.penup()
    turtle.goto(-50, 220)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(20)
    turtle.end_fill()

def main():
    turtle.speed(1)
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawHat()

    turtle.done()

if __name__ == "__main__":
    main()