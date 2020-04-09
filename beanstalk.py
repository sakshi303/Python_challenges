print("The Magic Beanstalk")
height = 100
hour = int(input("Enter the number of hours: - "))
print(hour)
print("After 1 hour, the beanstalk was 100 cm")
for i in range(1,hour) :
  height = height*1.5 + 30
 # print(height)
  print("After",i+1,"hours,the beanstalk was",height,"cm tall!")