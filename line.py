import turtle

pen = turtle.Turtle()
pen.color("black")
pen.fillcolor("grey")
pen.pensize(5)
pen.shape("turtle")


def draw_squares(x, y, edgeLength):
    pen.begin_fill()
    pen.up()
    pen.goto(x, y)
    pen.down()
    for i in range(0, 4):
        pen.forward(100)
        pen.left(90)
    pen.end_fill()


for x in range(-200, 200, 120):
    draw_squares(x, 200, 30)
