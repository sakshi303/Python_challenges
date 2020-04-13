import turtle
myPen = turtle.Turtle()
myPen.shape("arrow")

myPen.color("gold")
myPen.fillcolor("orange")
myPen.pensize(5)

def drawCavity(x,y,edgeLenght):
  myPen.penup()
  myPen.goto(x,y)
  myPen.pendown()
  myPen.begin_fill()
  for i in range(0,6):
      myPen.forward(20)
      myPen.left(60)
  myPen.end_fill()

for x in range(-30,10,60):
    drawCavity(x,230,20)

for x in range(-60,60,60):
    drawCavity(x,210,20)

for x in range(-90,90,60):
    drawCavity(x,190,20)

for x in range(-120,120,60):
    drawCavity(x,170,20)

for x in range(-150,150,60):
  drawCavity(x,150,20)

for x in range(-120,120,60):
  drawCavity(x,130,20)

for x in range(-150,150,60):
    drawCavity(x,110,20)

for x in range(-120,120,60):
    drawCavity(x,90,20)

for x in range(-150,150,60):
    drawCavity(x,70,20)

for x in range(-120,120,60):
    drawCavity(x,50,20)

for x in range(-90,90,60):
    drawCavity(x,30,20)

for x in range(-60,60,60):
    drawCavity(x,10,20)

for x in range(-30,30):
    drawCavity(x,-10,20)
    break