#%%
  
#----------DAY1----------

#%%

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





#%%










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



# %%



