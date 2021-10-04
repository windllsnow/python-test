#%%
  
#----------DAY1----------

#%%
print('='*20+'第'+'頁總共有'+'筆資料'+'='*10) #黏在一起
print('='*20,'第','頁總共有','筆資料','='*10) #，等於 空格

print(len('95637+12444'))   #'  ' 字元長度(個數)
#%%

numbers=[100,10,21,35,40,50]

result=[num +3  for num in numbers   if num % 7==0]#能除與7 的數字+3
print(result)  

#%%

print('Hello \t world \n \t'*5)
print("Hello\t"+ input ("What is your name?")+ "\t!")


# %%
x=input("What is your name?  ")
print(f"Your name is  {x:30s}  ")
print(f"共有{len(x):10d}字母")

# %%
a=input("a:")
b=input("b:")

c=a
a=b
b=c

print("a="+a)
print("b="+b)

# %%
city=input("Where are you come from?  ")
country=input("Where are you grew up?  ")
pet=input("What kind of pets do you ever have?  ")

print(f"Let me introduce your new band name can be  {city:4s} {country:4s} {pet:4s} band!  ")

# %%

#------------DAY2-----------------


# %%
print("Hello"[0])

print((10_10.10)+1.0)
q11='abbey Road'

print(q11[4]+q11[5]+q11[6])  # 空白鍵 也算

#%%
w=str(input("Please  key  two_digit_number:") )
w1=w[0]
w2=w[-1]
w11=int(w1)
w22=int(w2)
print(f"your number counter is  {w11+w22}")

#%%

we=int(input("What is your current  age?   "))
totallife=90

months=int((totallife-we)*12)
weeks=int((totallife-we)*52)
days=int((totallife-we)*365)
print("If you can live 90 years! And  \n")
print(f"You'll have {days:1d} days,{weeks:1d} weeks and {months:1d} months left")



#%%
poi=int(input("ANy number which you like:"))

sumq=0

for ii in str(poi):
    sumq+=int(ii)
   
   
print(sumq)

#%%
def each_unit_sum(number):
    """
    :param number :
    :return:
    """

    sum_value=0
    for item in str(number):
        sum_value+=int(item)
    return sum_value

print(each_unit_sum(1234))


# %%

s1=int(input("Begining?(yes=1,no=0)"))
s2=bool(s1)

while s2!=False:


    print("Welcome to the tip calculator! ")
    x1=float(input("What was the total bill which you had? "))
    y1=float(input("How many people to split the bill? "))
    z1=float(input("What percentage tip would you like to give?(10,12,15) ?  "))
    t1=float((x1/y1)*(100+z1)/100)
    print(f"Each person should pay{t1:10.2f} ")
    
    s1=int(input("this repl has exited, run again?(yes=1,no=0)"))
    s2=bool(s1)


# %%

#------------DAY3-----------------

#%%

xx=int(input('Which number you want to check? (Integer) '))
if xx==0:
    print(f'your number is {xx} , is not even and odd number')
elif xx%2==0:
    print("your number is even number")
else:
    print('your number is odd  number ')


# %%
#____________門票_____________
print("Welcome to the rollercoaster!\m ")
heighter=int(input('What is your height in cm? ' ))
bill=0

if heighter >=120:
    print(' You can ride the rollercoaster! \n ')
    age=int(input("What is your age? "))
    if age>=45 and age<=55:
        print("Everything is going to be ok. Have a free ride on us!")
    elif age >= 18:
        bill+=12
        print("adult tickets $12 once")
    elif age >= 12:
        bill+=7
        print("Youth tickets $7 once")
    else:
        bill+=5
        print("Child tickets $5 once")

    wants_photos=input("Do you want a photo taken ? Y or  N. ")
    if wants_photos == "Y" or wants_photos=="y":
        bill += 3
    print(f'you bill is {bill} dollars')
else:
    print("Sorry,you have to grow taller before you can ride")


# %%
#____________閏年_______________*****__________難__

zzz=int(input("This  year is ?  "))
if zzz % 4 ==0:
    if zzz % 100 ==0:
        if zzz % 400==0:
            print(f"This year {zzz} is Leap year")
        else:
            print(f"This  year {zzz} is not Leap year")   
    else:
        print(f"This  year {zzz} is  Leap year")   
else:
    print(f"This  year {zzz} is not Leap year")    
    
# %%
print("Welcome to Python Pizza Deliveries! ")
size=input("What siz pizza do you want? S  ,M ,or  L")
add_peperoni=input("Do you want pepperoni? Y or N")
extra_cheese=input("Do you want extra cheese? Y or N ")
bill=0
if size =="S":
    bill+=15
    if add_peperoni=="Y":
        bill+=2
        if extra_cheese=="Y":
            bill+=1
            print(f"Your final bills is ${bill}")
        else:
            print(f"Your final bills is ${bill}")
    else:
        print(f"Your final bills is ${bill}")
elif size =="M":
    bill+=20
    if add_peperoni=="Y":
        bill+=3
        if extra_cheese=="Y":
            bill+=1
            print(f"Your final bills is ${bill}")
        else:
            print(f"Your final bills is ${bill}")
    else:
        print(f"Your final bills is ${bill}")
else:
    bill+=25
    if add_peperoni=="Y":
        bill+=3
        if extra_cheese=="Y":
            bill+=1
            print(f"Your final bills is ${bill}")
        else:
            print(f"Your final bills is ${bill}")
    else:
        print(f"Your final bills is ${bill}")
#s 15  2 1
#m 20  3 1
#l 25  3 1

#%%
print("Welcome to Python Pizza Deliveries! ")
size=input("What siz pizza do you want? S  ,M ,or  L")
add_peperoni=input("Do you want pepperoni? Y or N")
extra_cheese=input("Do you want extra cheese? Y or N ")
bill=0
if size =="S":
    bill+=15
elif size=="M":
    bill+=20
else:
    bill+=25
if add_peperoni =="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if extra_cheese=="Y":
    bill+=1
print(f"Your final bill is ${bill}")


# %%
#________________LOVE　Caculator_____________________________

print("Welcome to the Love Calculator! ")
name1=input("What is  your name?\n")
name2=input("What is  their name? \n")
n1_01=name1.lower()
n2_01=name2.lower()
n3=n1_01+n2_01


n31=n3.count("t")+n3.count("r") +n3.count("u")+ n3.count("e")  # int
n32=n3.count("l")+n3.count("o") +n3.count("v")+ n3.count("e")  # int

n333=str(n31)+str(n32)   # str

n33=int(n333)   #int



if n33 >90 or n33<10:
    print(f"Yours' Love score is {n33},you go together like coke and mentos")
elif n33>=40 and n33<=50:
    print(f"Yours' Love score is {n33},you are alright together")
else:
    print(f"Yours' Love score is {n33}")

# you are alright together ( 40-50
# you go together like coke and mentos  ( <10 or >90


# %%
#____________________Day4________________________

# %%



# %%




# %%



