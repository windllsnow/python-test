import random
lotterys=random.sample(range(1,51),6)
specialNum=lotterys.pop()
print("第xxx期的大樂透號碼",end=" \t")
for lottery in sorted(lotterys):
    print(lottery,end="\n")
print(" 特別號:%d " % specialNum)

#%%
import random

def randomNum():
    for iteration, num in enumerate(range(4)):
        first = random.randint(1,10)
        second = random.randint(1,10)
        third = random.randint(1,10)
        fourth = random.randint(1,10)
    print('Lotto number 1', first)
    print('Lotto number 2', second)
    print('Lotto number 3', third)
    print('Lotto number 4', fourth)
    print('the number of tries', iteration)
print(randomNum())