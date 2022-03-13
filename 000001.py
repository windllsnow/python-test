
# %%


import random as rm
a = rm.random()
print(a)


print(123)


# %%

n = int(input())
a = 0

for i in range(n):
    a = int(input())
    if a > 5:
        print(a, ",", end="")


# %%
n = 10


bb = []

for i in range(n):
    bb.append(i)
    print(bb)


print(bb)
print(type(bb))

# what the fuck 
# 要先轉 str 再 轉

Str_bb ="".join([str(_)for _ in bb]) 
    
print(Str_bb)
    

# %%
if __name__ == '__main__':
    n = int(input())
    bb = []

    for i in range(1,n+1):
        bb.append(i)
    
    Str_bb ="".join([str(_)for _ in bb]) 
    
    print(Str_bb)
#%%


