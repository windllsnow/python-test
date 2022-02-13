
# %%

import random


def guessing_game():
    x = random.uniform(0, 100)

    xx1 = round(x)

    test = True
    while test:
        y = int(input("猜猜數字(0-99) : "))
        if (y == xx1):
            print("猜對了")
            print(f"your number is {y}")
            test = False
        elif(y > xx1):
            print("猜太高，重來")
            print(f"your number is {y}")
        else:
            print("太低了，重來")
            print(f"your number is {y}")


guessing_game()

# %%
