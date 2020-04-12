import turtle
pen = turtle.Turtle()

pen.shape("circle")
pen.color("black")
pen.fillcolor("grey")
pen.pensize(3)

def drawing(x,y,edgeLength):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.begin_fill()
    for i in range(0,4):
        pen.forward(edgeLength)
        pen.left(90)
    pen.end_fill()

    for x in range(-150,150,100):
        drawing(x,100,40)
