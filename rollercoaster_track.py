import turtle
track = turtle.Turtle()
track.speed(100)

track.color("pink")
track.pensize(5)
track.shape("turtle")

def go_straight(distance,speed):
    for i in range(0,distance,speed):
        track.forward(speed)

def turnLeft(angle,radius):
    turn = 10*3.14*radius/360
    for i in range(0,angle,5):
        track.left(5)
        track.forward(turn)

def turnRight(angle,radius):
    rturn = 10*3.14*radius/360
    for i in range(0,angle,5):
        track.right(5)
        track.forward(rturn)


go_straight(100,3)
turnRight(90,30)
go_straight(75,6)
turnLeft(180,60)
go_straight(200,3)
turnLeft(360,70)
go_straight(100,3)
turnLeft(90,50)
go_straight(250,4)
turnRight(360,50)
go_straight(100,3)
turnLeft(90,30)
go_straight(185,6)
turnLeft(90,30)
go_straight(150,3)
