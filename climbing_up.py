import time
import os

def animate_up():
    top = 10
    right = 1
    step = 1
    while top>0:
        print("\n" *top)
        for i in range(1,2):
            print(("   "*right) +"o")
            right=right+1
        top=top-1
        time.sleep(0.5)
        os.system('clear')

        # time.sleep(1)


def animate_right():
    right = 2
    top = 0
    while right < 5:
        print((" " * right) + "o")
        time.sleep(1)
        os.system('clear')
        right += 1


animate_up()