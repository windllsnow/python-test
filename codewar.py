#%%
x =int(input("Input number: "))
if type(x) != int:
    print("Error")
    pass
else:
    print((x*50)+6)

#
def problem(a):
    if type(a) == str:
        return "Error"
    else:
        answer = a*50+6
        return answer
#
problem = lambda a: 50*a+6 if isinstance(a, (int, float))  else "Error" 
#
# chr str
#   codewar 不用 input 直接打在 def  
# attempt-->test
# return  出來是值


#%% 

def  square_sum(numbers):
    def square(numbers):
        return map(lambda x: x**2, numbers)
    y= square(numbers)
    Sum= sum(y)
    return print(Sum)

square_sum([1, 2, 3, 4, 5])

#%%




#%% 



