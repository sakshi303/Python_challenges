from random import randint

numberToGuess = randint(1,100)
userguess = int(input("Enter your guess between 1-100: "))

while numberToGuess!= userguess:
    if numberToGuess < userguess:
        userguess = int(input("Please guess lower: "))

    if numberToGuess > userguess:
        userguess = int(input("Please guess higher: "))


if numberToGuess == userguess:
  print("You win")

