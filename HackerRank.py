

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

n = int(input("輸入幾個數"))
a = 0
print("大於 5 的數 有\t")
for i in range(n):





    a = int(input("數字:"))

    if a > 5:

        print(f"{a},", end="")


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


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    kk = []

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                kk.append([i, j, k])
                if i+j+k == n:
                    kk.pop()

                else:
                    pass

    print(kk)

    #    確認append 裡 用原本的型態
    #   用迴圈 ，所以遇到時，必為最後一個，pop刪掉
    #    要最後結果不用過程，出迴圈在print


# %%
'''
取n 數 input
k=0 while  K++  K=n 跳出
t=[]
input 加元素進去
sort sorted 由大到小排列
取索引值 第二個 i=1(0->1)
print 出來
'''

# %%
