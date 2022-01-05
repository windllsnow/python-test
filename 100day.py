# %%

# ----------DAY1----------

# %%

# 集合的 pop()

from replit import clear
import random as r
import random as rad
import random
from os import name
print('='*20+'第'+'頁總共有'+'筆資料'+'='*10)  # 黏在一起
print('='*20, '第', '頁總共有', '筆資料', '='*10)  # ，等於 空格

print(len('95637+12444'))  # '  ' 字元長度(個數)
# %%


# list.pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
list1 = ['Google', 'Runoob', 'Taobao']
list_pop = list1.pop(1)
print(f"删除的项为 :{list_pop}")
print(f"列表现在为 : {list1}")

print("_"*58)

# 字典的 pop()
site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop__obj = site.pop('name')
print(pop__obj)
print(site)

print("_"*58)

# 集合的 pop()
# 执行下面的代码,并查看输出结果:
print('pop()函数的输出结果 看这里:')
s1 = {4, 2, 1, 5}  # 集合里只有数字
s2 = {'你', '我', '他'}  # 集合里无数字
s3 = {3, 2, 4, '你', 'X'}  # 集合里既有数字又有非数字
s1.pop()  # 元素是数字时, 删除最小的数字, 其余数字升序排列
s2.pop()  # 元素非数字时, 随机删除一个元素, 其余元素随机排序
s3.pop()  # 元素既有数字又含非数字时, 如果删除的是数字, 则一定删最小的, 否则随机删除一个非数字元素
print(s1)
print(s2)
print(s3)  # 这个代码执行后, 输出的结果是随机的
'''
总结:

1、如果集合的元素都是数字, 删除时, 删掉的是最小的数字, 其余数字升序排列

2、如果集合的元素是非数字, 删除时, 删掉的是随机的元素, 其余元素随机排列

3、如果集合里既有数字又有非数字元素, 删除时:

若删掉的是数字, 则一定是删掉了最小的, 其他数字升序排列, 非数字元素随机排列;
若删掉的非数字, 则一定是随机删掉了一个, 其他数字升序排列, 非数字则随机排列.

'''
# %%

numbers = [100, 10, 21, 35, 40, 50]

result = [num + 3 for num in numbers if num % 7 == 0]  # 能除與7 的數字+3
print(result)

# %%

print('Hello \t world \n \t'*5)
print("Hello\t" + input("What is your name?") + "\t!")


# %%
x = input("What is your name?  ")
print(f"Your name is  {x:30s}  ")
print(f"共有{len(x):10d}字母")

# %%
a = input("a:")
b = input("b:")

c = a
a = b
b = c

print("a="+a)
print("b="+b)

# %%
city = input("Where are you come from?  ")
country = input("Where are you grew up?  ")
pet = input("What kind of pets do you ever have?  ")

print(
    f"Let me introduce your new band name can be  {city:4s} {country:4s} {pet:4s} band!  ")

# %%

# ------------DAY2-----------------


# %%
print("Hello"[0])

print((10_10.10)+1.0)
q11 = 'abbey Road'

print(q11[4]+q11[5]+q11[6])  # 空白鍵 也算

# %%
w = str(input("Please  key  two_digit_number:"))
w1 = w[0]
w2 = w[-1]
w11 = int(w1)
w22 = int(w2)
print(f"your number counter is  {w11+w22}")

# %%

we = int(input("What is your current  age?   "))
totallife = 90

months = int((totallife-we)*12)
weeks = int((totallife-we)*52)
days = int((totallife-we)*365)
print("If you can live 90 years! And  \n")
print(
    f"You'll have {days:1d} days,{weeks:1d} weeks and {months:1d} months left")


# %%
poi = int(input("ANy number which you like:"))

sumq = 0

for ii in str(poi):
    sumq += int(ii)


print(sumq)

# %%


def each_unit_sum(number):
    """
    :param number :
    :return:
    """

    sum_value = 0
    for item in str(number):
        sum_value += int(item)
    return sum_value


print(each_unit_sum(1234))


# %%

s1 = int(input("Begining?(yes=1,no=0)"))
s2 = bool(s1)

while s2 != False:

    print("Welcome to the tip calculator! ")
    x1 = float(input("What was the total bill which you had? "))
    y1 = float(input("How many people to split the bill? "))
    z1 = float(input("What percentage tip would you like to give?(10,12,15) ?  "))
    t1 = float((x1/y1)*(100+z1)/100)
    print(f"Each person should pay{t1:10.2f} ")

    s1 = int(input("this repl has exited, run again?(yes=1,no=0)"))
    s2 = bool(s1)


# %%

# ------------DAY3-----------------

# %%

xx = int(input('Which number you want to check? (Integer) '))
if xx == 0:
    print(f'your number is {xx} , is not even and odd number')
elif xx % 2 == 0:
    print("your number is even number")
else:
    print('your number is odd  number ')


# %%
# ____________門票_____________
print("Welcome to the rollercoaster!\m ")
heighter = int(input('What is your height in cm? '))
bill = 0

if heighter >= 120:
    print(' You can ride the rollercoaster! \n ')
    age = int(input("What is your age? "))
    if age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    elif age >= 18:
        bill += 12
        print("adult tickets $12 once")
    elif age >= 12:
        bill += 7
        print("Youth tickets $7 once")
    else:
        bill += 5
        print("Child tickets $5 once")

    wants_photos = input("Do you want a photo taken ? Y or  N. ")
    if wants_photos == "Y" or wants_photos == "y":
        bill += 3
    print(f'you bill is {bill} dollars')
else:
    print("Sorry,you have to grow taller before you can ride")


# %%
# ____________閏年_______________*****__________難__

zzz = int(input("This  year is ?  "))
if zzz % 4 == 0:
    if zzz % 100 == 0:
        if zzz % 400 == 0:
            print(f"This year {zzz} is Leap year")
        else:
            print(f"This  year {zzz} is not Leap year")
    else:
        print(f"This  year {zzz} is  Leap year")
else:
    print(f"This  year {zzz} is not Leap year")

# %%
print("Welcome to Python Pizza Deliveries! ")
size = input("What siz pizza do you want? S  ,M ,or  L")
add_peperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 15
    if add_peperoni == "Y":
        bill += 2
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bills is ${bill}")
        else:
            print(f"Your final bills is ${bill}")
    else:
        print(f"Your final bills is ${bill}")
elif size == "M":
    bill += 20
    if add_peperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bills is ${bill}")
        else:
            print(f"Your final bills is ${bill}")
    else:
        print(f"Your final bills is ${bill}")
else:
    bill += 25
    if add_peperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bills is ${bill}")
        else:
            print(f"Your final bills is ${bill}")
    else:
        print(f"Your final bills is ${bill}")
# s 15  2 1
# m 20  3 1
# l 25  3 1

# %%
print("Welcome to Python Pizza Deliveries! ")
size = input("What siz pizza do you want? S  ,M ,or  L")
add_peperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_peperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}")


# %%
# ________________LOVE　Caculator_____________________________

print("Welcome to the Love Calculator! ")
name1 = input("What is  your name?\n")
name2 = input("What is  their name? \n")
n1_01 = name1.lower()
n2_01 = name2.lower()
n3 = n1_01+n2_01


n31 = n3.count("t")+n3.count("r") + n3.count("u") + n3.count("e")  # int
n32 = n3.count("l")+n3.count("o") + n3.count("v") + n3.count("e")  # int

n333 = str(n31)+str(n32)   # str

n33 = int(n333)  # int


if n33 > 90 or n33 < 10:
    print(f"Yours' Love score is {n33},you go together like coke and mentos")
elif n33 >= 40 and n33 <= 50:
    print(f"Yours' Love score is {n33},you are alright together")
else:
    print(f"Yours' Love score is {n33}")

# you are alright together ( 40-50
# you go together like coke and mentos  ( <10 or >90


# %%
# ____________________Day4________________________

# %%


random_integer = random.randint(0, 1)
print(random_integer)

# 0.000000~0.99999999...
random_float = random.random()
print(random_float)

# 0.000000~4.99999999...
random_float1 = random_float*5
print(random_float1)

love_score1 = random.randint(1, 100)
print(f"Your love score is {love_score1}")

# %%

pp1 = random.randint(0, 1)
p = int(input("Please key any integer to move on! Exit please key  -1 "))
while p != -1:
    if pp1 == p:
        print('Heads')
        break
    else:
        print("Tails")
        break
print("\n Game finished")
# %%
# list

names_string = input("Give me  everyone's names , seperated by a comma.")
names1 = names_string.split(",")  # 預設一格 空格

kkk001 = random.choice(names1)
print(f" {kkk001} is your turn to buy lunch !  XDD")
# ________________上下一樣結果__________
num_item1 = len(names1)
num_cc = random.randint(0, num_item1-1)
print(f" {num_cc} is your turn to buy lunch !  XDD")


# %%
# 藏寶圖
# 題目  先 欄 後 列

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?")

pp22 = str(position)
x001 = pp22[1]
y001 = pp22[0]
x0001 = int(x001)
y0001 = int(y001)
map[x0001-1][y0001-1] = "x"
print("____"*10)


print(f"{row1}\n{row2}\n{row3}")
# %%

# 剪刀 石頭 布
# _________________超難______________________-------


rrr = int(input(
    "What do you want to choice? Type 0 for Rock , 1 for Paper,2 for Scissors"))
r1 = ["石頭", "布", "剪刀"]  # 給人
r2 = ["石頭", "布", "剪刀"]  # 給 機器

r2_choice = rad.randint(0, len(r2)-1)  # 數字  注意 len()-1
try:
    print(f"你出的是{r1[rrr]}")
    print(f"機器出的是{r2[r2_choice]}")

    while rrr == r2_choice:
        print("woops!,Please 重輸!")
        rrr = int(input(
            "What do you want to choice? Type 0 for Rock , 1 for Paper,2 for Scissors"))
        print(f"你出的是{r1[rrr]}")
        print(f"機器出的是{r2[r2_choice]}")
    if rrr > r2_choice:
        if r2_choice == 0 and rrr == 2:
            print("you lose")
        else:
            print("you win")
    else:
        if rrr == 0 and r2_choice == 2:
            print("you win")
        else:
            print("you lose")
except:
    print("oops GG ,game over ,because you key number not 0,1 or 2")


# %%


# _______________day5__________________


# %%


fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit+"Pie")
print(fruits)


# %%
student_heights = input("Input a list of student heights").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# don't use  sum()、len

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)


print(f"平均身高{total_height/number_of_students:4.4f} cm")


# %%

# _______________想一下_______________________
student_score = input("Input a list of student score").split()

for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)
highest_score = 0
for score in student_score:
    # 如[100,200,300];100>0; highest=100   =>     200>100;  highest=200...
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is :{highest_score}")

# %%
sum1 = 0
n = 0
for n in range(1, 101, 2):
    n += 1      # 1+1 3+1 .....
    sum1 = sum1+n
print(sum1)


sum2 = 0
for n in range(2, 101, 2):  # 2 4 ....
    sum2 += n
print(sum2)


sum3 = 0
for n in range(1, 101):
    if n % 2 == 0:
        sum3 += n
print(sum3)


# %%

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0 or n % 5 == 0:
        if n % 3 == 0:
            print("Fizz")
        else:
            print("Buzz")
    else:
        print(n)


# %%

# __________________password____超難!!______________________
letterss = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numberss = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the pypassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numberss = int(input("How many numbers would you like? \n"))


num00 = nr_letters+nr_symbols+nr_numberss  # 確認 密碼 位數
print(num00)

l2 = r.sample(letterss, nr_letters)
s2 = r.sample(symbols, nr_symbols)  # 由 x字串中隨機n個字元   (type: list)
n2 = r.sample(numberss, nr_numberss)


fin2 = l2+s2+n2       # list 相加

print(fin2)

kk = r.sample(fin2, 6)  # 取6個 取後不放回
print(kk)
StrQ = "".join(kk)      # list 轉 str
print(f"你的新密碼: \t {StrQ} \t")

# %%
# __________________password____超難!!______________________
letterss = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numberss = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the pypassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numberss = int(input("How many numbers would you like? \n"))

# _________________________________________________easy__________________________________
password = ""
for char in range(1, nr_letters+1):
    password += r.choice(letterss)
for char in range(1, nr_symbols+1):
    password += r.choice(symbols)
for char in range(1, nr_numberss+1):
    password += r.choice(numberss)
print(password)


# %%

# %%
# __________________password____超難!!______________________
letterss = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numberss = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the pypassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numberss = int(input("How many numbers would you like? \n"))


# _________________________________________________HARD__________________________________

password_list1 = []
for char in range(1, nr_letters+1):
    password_list1 += r.choice(letterss)
for char in range(1, nr_symbols+1):
    password_list1 += r.choice(symbols)
for char in range(1, nr_numberss+1):
    password_list1 += r.choice(numberss)
print(password_list1)

r.shuffle(password_list1)
print(password_list1)
password1 = ""
for char in password_list1:
    password1 += char
print(f"Your password  is {password1}")

# %%
# _________________________________________DAY  6____________________________________


# %%

# def
# w hile   Loop


# %%

# __________________________________DAY7___________________________________________


# %%

# __________劊子手___超難 =='''  //我的mind  都扣1  出去再判斷

word_list = ["ardvark", "baboon", "camel"]

choice_word = random.choice(word_list)
print(f"pssst, the solution is {choice_word}.")

display = []
word_length = len(choice_word)

for _ in range(word_length):
    display += "_"
print(display)


game_times = 0

while game_times < 6:

    guess = input("Guess a letter:").lower()
    print(f"your letter you key one second before is' {guess} ' ")

    for position in range(word_length):
        letter = choice_word[position]

        if letter == guess:
            display[position] = letter
    print("The rusult is \n")
    print(display)
    game_times += 1
    if "_" not in display:
        game_times += 6
        print("your win")

if game_times == 6:
    print("you lose, die!")
else:
    print("Concretulation")


# %%
# __________劊子手___超難 ==''' 扣命

word_list = ["ardvark", "baboon", "camel"]

choice_word = random.choice(word_list)
print(f"pssst, the solution is {choice_word}.")

display = []
word_length = len(choice_word)

for _ in range(word_length):
    display += "_"
print(display)


end_of_game = False
lives = 6

while end_of_game == False:

    guess = input("Guess a letter:").lower()
    print(f"your letter you key one second before is' {guess} ' ")
    for position in range(word_length):
        letter = choice_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in choice_word:

        lives -= 1  # bug 是 如果輸入一樣 無限迴圈
        if lives == 0:
            end_of_game = True
            print("you lose!")

    print("The rusult is \n")
    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game == True
        print("your win")


# %%

# __________劊子手___超難 ==''' 扣命 final
# 有bug  成功無法  跳出  ，一定要失敗  =='''

word_list = [
    'abruptly',
    'absurd',
    'abyss',
    'affix',
    'askew',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bagpipes',
    'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'bookworm',
    'boxcar',
    'boxful',
    'buckaroo',
    'buffalo',
    'buffoon',
    'buxom',
    'buzzard',
    'buzzing',
    'buzzwords',
    'caliph',
    'cobweb',
    'cockiness',
    'croquet',
    'crypt',
    'curacao',
    'cycle',
    'daiquiri',
    'dirndl',
    'disavow',
    'dizzying',
    'duplex',
    'dwarves',
    'embezzle',
    'equip',
    'espionage',
    'euouae',
    'exodus',
    'faking',
    'fishhook',
    'fixable',
    'fjord',
    'flapjack',
    'flopping',
    'fluffiness',
    'flyby',
    'foxglove',
    'frazzled',
    'frizzled',
    'fuchsia',
    'funny',
    'gabby',
    'galaxy',
    'galvanize',
    'gazebo',
    'giaour',
    'gizmo',
    'glowworm',
    'glyph',
    'gnarly',
    'gnostic',
    'gossip',
    'grogginess',
    'haiku',
    'haphazard',
    'hyphen',
    'iatrogenic',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jaundice',
    'jawbreaker',
    'jaywalk',
    'jazziest',
    'jazzy',
    'jelly',
    'jigsaw',
    'jinx',
    'jiujitsu',
    'jockey',
    'jogging',
    'joking',
    'jovial',
    'joyful',
    'juicy',
    'jukebox',
    'jumbo',
    'kayak',
    'kazoo',
    'keyhole',
    'khaki',
    'kilobyte',
    'kiosk',
    'kitsch',
    'kiwifruit',
    'klutz',
    'knapsack',
    'larynx',
    'lengths',
    'lucky',
    'luxury',
    'lymph',
    'marquis',
    'matrix',
    'megahertz',
    'microwave',
    'mnemonic',
    'mystify',
    'naphtha',
    'nightclub',
    'nowadays',
    'numbskull',
    'nymph',
    'onyx',
    'ovary',
    'oxidize',
    'oxygen',
    'pajama',
    'peekaboo',
    'phlegm',
    'pixel',
    'pizazz',
    'pneumonia',
    'polka',
    'pshaw',
    'psyche',
    'puppy',
    'puzzling',
    'quartz',
    'queue',
    'quips',
    'quixotic',
    'quiz',
    'quizzes',
    'quorum',
    'razzmatazz',
    'rhubarb',
    'rhythm',
    'rickshaw',
    'schnapps',
    'scratch',
    'shiv',
    'snazzy',
    'sphinx',
    'spritz',
    'squawk',
    'staff',
    'strength',
    'strengths',
    'stretch',
    'stronghold',
    'stymied',
    'subway',
    'swivel',
    'syndrome',
    'thriftless',
    'thumbscrew',
    'topaz',
    'transcript',
    'transgress',
    'transplant',
    'triphthong',
    'twelfth',
    'twelfths',
    'unknown',
    'unworthy',
    'unzip',
    'uptown',
    'vaporize',
    'vixen',
    'vodka',
    'voodoo',
    'vortex',
    'voyeurism',
    'walkway',
    'waltz',
    'wave',
    'wavy',
    'waxy',
    'wellspring',
    'wheezy',
    'whiskey',
    'whizzing',
    'whomever',
    'wimpy',
    'witchcraft',
    'wizard',
    'woozy',
    'wristwatch',
    'wyvern',
    'xylophone',
    'yachtsman',
    'yippee',
    'yoked',
    'youthful',
    'yummy',
    'zephyr',
    'zigzag',
    'zigzagging',
    'zilch',
    'zipper',
    'zodiac',
    'zombie',
]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = '''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    '''


print(logo)


end_of_game = False
lives = len(stages)-1


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
print(f"pssst, the solution is {chosen_word}.")
for _ in range(word_length):
    display += "_"
print(display)


while not end_of_game:

    guess = input("Guess a letter:").lower()
    clear()

    if guess in display:
        print(f"you've already guessed{guess}")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
    print(f"{''.join(display)}")

    if guess not in chosen_word:
        print(
            f"you guessd{guess},that's not in the word. your lost your life ")
        lives -= 1  # bug 是 如果輸入一樣 無限迴圈
        if lives == 0:
            end_of_game = True
            print("you lose!")

    if "_" not in display:
        end_of_game == True
        print("your win")

    print(stages[lives])

# fuck  fuck yes  >_<
# fuck  fuck yes  >_<


# %%

# ----Day8----------------
# -----函數--
# %%
def greet(a, b, c):

    print("hello")
    print("wear")
    print("dread")
    return print(f'hello ! your answers is {a*b*c}')


def greet23(a, b, c):

    return f'hello ! your answers is {(a*b*c)**2}'


greet(1, 2, 3)
greet23(1, 2, 3)


# %%
# prime number 質數


def prime_check(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number!")
    else:
        print("It's not a prime number!")


o = int(input("Check your number: "))
prime_check(number=o)


# %%


# %%

# Caesar Cipher

key = True

while key:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input(
        "Type 'encode'  to encrypt, type 'decode' to decrypt(make sure your word correct!!!): \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number(1~26): \n"))

    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        shift_amount = shift_amount % 26
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
        print(f"Here is the {direction}d result: {end_text}")

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    ww = input("Want to play again ? (please answer  'yes' or 'no')")
    if (ww == "yes") | (ww == "YES") | (ww == "Yes"):
        key = True
    elif (ww == "no") | (ww == "NO") | (ww == "No"):
        key = False
        print("Bye.\n")

print("Bye!")


# %%
# Day 9  Dictionary & Nesting

# %%

program = {
    "bug": "I'm a bug",
    "function": "I'm a function",
    "loop": "I'm a loop"
}

for keyy in program:
    print(keyy)
    print(program[keyy]+"\n")


# %%


# Grading Program

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}


student_grades = {}

for j in student_scores:
    score = student_scores[j]
    if score > 90:
        student_grades[j] = "Outstanding"
    elif score > 80:
        student_grades[j] = "Exceeds Expectations"
    elif score > 70:
        student_grades[j] = "Acceptable"
    else:
        student_grades[j] = "Bye!!!!!!!!!!!"


print(student_grades)

# %
# %%

# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visited": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visited": 55,
    },
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities_visited"] = cities_visited
    new_country["total_visited"] = times_visited
    travel_log.append(new_country)


add_new_country("Russian", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


# %%
# Q&A
dict44 = {
    "a": 1,
    "b": 2,
    "c": 3,

}

dict44[1] = 7


print(dict44)

for k in dict44:
    dict44[k] += 1
    print(dict44[k])
