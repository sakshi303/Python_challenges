#The honeycomb challenge - www.101computing.net/honeycomb-challenge/
import turtle
myPen = turtle.Turtle()

myPen.shape("turtle")
myPen.color("gold")
myPen.fillcolor("turquoise")

myPen.pensize(5)
#myPen.delay(10) #Set the speed of the turtle

#A Procedue to draw a pentagonal cavity at a given (x,y) position.
def drawCavity(x,y,edgeLength):
  myPen.penup()
  myPen.goto(x,y)
  myPen.pendown()
  myPen.begin_fill()
  for i in range(0,6):
      myPen.forward(edgeLength)
      myPen.left(60)
  myPen.end_fill()


#Main Program Starts Here
#Comlpete this code to draw a full honeycomb pattern
for x in range(-150,150,30):
  drawCavity(x,150,20)





myPen.hideturtle()