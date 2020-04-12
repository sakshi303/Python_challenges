from random import randint
import random
from typing import List, Any

capsletter1 = randint(65,90)
capsletter2 = randint(65,90)
lowercaseletter1 = randint(97,122)
lowercaseletter2 = randint(97,122)
number1 = randint(0,9)
number2 = randint(0,9)
punctuation1 = randint(32,47)
punctuation2 = randint(91,96)

capsletter1 = chr(capsletter1)
capsletter2 = chr(capsletter2)
lowercaseletter1 = chr(lowercaseletter1)
lowercaseletter2 = chr(lowercaseletter2)
punctuation1 = chr(punctuation1)
punctuation2 = chr(punctuation2)

def shuffle(str):
    tpassword = list(str)
    random.shuffle(tpassword)
    return ''.join(tpassword)

password = capsletter1 + capsletter2 + lowercaseletter1 + lowercaseletter2 +\
           str(number1) + str(number2) + str(punctuation1)+ str(punctuation2)
#print(password)

password = shuffle(password)
print(password)



