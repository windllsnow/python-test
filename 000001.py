
# %%
#
# HackerRank
#
#
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

Str_bb = "".join([str(_)for _ in bb])

print(Str_bb)


# %%
if __name__ == '__main__':
    n = int(input())
    bb = []

    for i in range(1, n+1):
        bb.append(i)

    Str_bb = "".join([str(_)for _ in bb])

    print(Str_bb)
# %%
'''
List.extend(iterable) 將每個 iterator 加入 list
'''
xx = list(range(5))
print(xx)
yy = list(range(2))
print(yy)
xx.extend(yy)
print(xx)

'''
List.append(object) 將 object 加入 list
'''
xx = list(range(5))
print(xx)
yy = list(range(2))
print(yy)

xx.append(yy)
print(xx)
'''
從上面兩個例子可知道，
extend 是取出 object 的所有 element/iterator 扔進list 裡面，
而 append 則直接把 object 塞進 list 裡面，
不管 object 是哪種類型的資料結構。
'''
# %%


# %%
