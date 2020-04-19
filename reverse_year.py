year = int(input("Enter any digit number: "))
counter = 0
lennum = len(str(year))
print('Reverse of given digit is:',end='')
#print(lennum)
while counter<lennum:
   a= year%10
   year = int(year/10)
   print(a, end='')
   counter +=1
