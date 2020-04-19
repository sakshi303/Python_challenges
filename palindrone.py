test_name = str(input("Enter a word: "))
length = len(test_name)
test_name = test_name.lower()
reverse =test_name[length::-1]
print(test_name[length::-1])
if reverse == test_name:
    print("The given word is a palindrome")
else:
    print("The given word is not a palindrome")




