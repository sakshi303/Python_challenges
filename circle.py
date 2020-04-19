print("enter either a diameter or radius")
radius = float(input("Enter the radius of the circle. if no radius is mentioned, enter 0: "))
diameter = float(input("Enter the  diameter of circle. if no diameter is mentioned. Enter 0: "))
if radius == 0:
    radius = diameter/2
print(radius)
if diameter ==0:
    diameter = radius*2
print(diameter)
perimeter = diameter *3.142
perimeter = round(perimeter,2)
area = 3.142*(radius*radius)
area = round(area,2)
print("The area of your circle is: ",area)
print("The circumference of your circle is: ",perimeter)
