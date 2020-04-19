print("enter either a diameter or radius")
radius = float(input("Enter the radius of the circle. if no radius is mentioned, enter 0: "))
diameter = float(input("Enter the  diameter of circle. if no diameter is mentioned. Enter 0: "))
height = float(input("Enter the height of the cylinder: "))
if radius == 0:
    radius = diameter/2
#print(radius)
if diameter ==0:
    diameter = radius*2
#print(diameter)
volume = 2*3.142*(radius*radius)*height
volume = round(volume,2)
print("The volume of the cylinder is: ",volume)
