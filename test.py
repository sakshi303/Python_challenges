str=list()
str=input('Enter your  String : ')
str=str.lower()
index=len(str)
str2=[]
while index>0:
    print(str[index-1])
    str2 += str[index-1]
    index=index-1
str2=str2.lower()
print(str2)
if str == str2:
    print("pallindrome")
else:
    print('Not Pallindrome')

#slicedString=str[strlen::-1] # slicing
#print (slicedString) # print the reversed string
#if str == slicedString:
#    print("pallindrome")
#else:
#    print('Not Pallindrome')