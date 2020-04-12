pupils = ["Joe","Sonny","Yassine","Emma","Ines","Satveer","Lily","Reuben","Lucy","Tom"]

counter = 0
pcounter = 0

for name in pupils:
    print(name)
    present = input("enter 'y' for yes and 'n'for no: ")
    counter = counter + 1
    if present == 'y':
        pcounter = pcounter + 1

print("Total number of students",counter)
print("Total number of students present",pcounter)
acounter = counter - pcounter
print("TOtal number of students absent", acounter)