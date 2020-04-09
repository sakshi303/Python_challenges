print("You need to enter you username in the following format: '07' for year 7, '08'for year 8, '11' for year 11 and so on. Then 00 for staff the initial of your first name followed by the last name .e.g jFrost. then '_S' for student, '_T' for teacher, '_A' for Admin Staff")
username = input("Enter your username here: ")
length = len(username)
if len(username)<6 or "_" not in username:
    print("Invalid username")
if len(username)<6 or "_" not in username:


 if "07" or "08" or "09" or "10" or"11" or "12" or "13" or "00" not in username[2:]:
    print("Invalid username")
if "07" in username[:2]:
   print("You are in year 7")
#print(username[:2])
if "08" in username[:2]:
   print("You are in year 8")
if "09" in username[:2]:
    print("You are in year 9")
if "10" in username[:2]:
    print("You are in year 10")
if "11" in username[:2]:
    print("You are in year 11")
if "12" in username[:2]:
    print("You are in year 12")
if "13" in username[:2]:
    print("You are in year 13")



if "_S" in username:
     print("you are a student")
if "_T" in username:
    print("you are a teacher")
if "_A" in username:
    print("You are an Admin Staff")



print("Your initial for your first name is",username[2])
print("Your last name is",username[3:-2])



