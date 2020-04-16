this_year = 2020
print("We are in 2020")
age = int(input("enter your age for 2020: "))
year = int(input("Enter the year you would like to know your age for: "))
year = year-this_year
for i in range(year,this_year):
    age = age+ year
    break
print("your age will be",age)

