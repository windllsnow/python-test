#%%

print(len('95637+12444'))   #'  ' 字元長度(個數)
#%%

numbers=[100,10,21,35,40,50]

result=[num +3  for num in numbers   if num % 7==0]
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

# %%

# %%

# %%
