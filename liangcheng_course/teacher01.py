#%%
import math
r=3
area=r**2*math.pi
print(area)

p=[2,5] #  中括號, 陣列
q=[8,9]
print(math.dist(p,q))#兩點間距離

#help(type)
#help(print)



#%%



name= input('name1')
score=input('score1')
print("姓名" +  name  +   ','   +  '分數'   +   score)# a+b+c+d+e 

name2=int(input('name2'))
score2=int(input('score2'))
print("成績="+str(name2+score2))
#int(input()) ,強改寫
#數字相加  改文字相加列印

#eval(input())
#%%

print(bool(1))
r=True
print(int(r))

#%%
#7/14
#7/16

#%%
money=50000
ir=0.015
n=5
for i in range(n):
    money*=(1+ir)  #    *=累乘   +=累加
    print(f'第{i+1}年的本金和:{int(money)}')
#%%

playerA=['john','james','curry','otani','wang']
playerB=['john','ben','wang']
for player in playerA:
    if player in playerB:
        playerA.remove(player)
        print(f'{player}是一約兩簽，已解約')
print('球隊的新名單是' , playerA)

#%%
playerA1=['john','james','curry','otani','wang']
playerB1=['john','ben','wang']
playersnew=[]
for playerk in playerA1:
    if playerk in playerB1:
        playersnew.append(playerk)
        print(f'{playerk}是一約兩簽，已解約')
print('已解約名單是' , playersnew)   

#%%
total=0
for j in range(1,11):
    total+=j
print(total)

a=list(range(1,101))
print(a)

total1=0
for k in a:
    if k%3==0:
        print(k)
        total1+=k
print(total1)
#%%
total4=0
i=0
while i<5:
    total4+=i
    i+=1
print(total4)

#%%
list=[4,2,1,-2,-5,-7]
#list1=sorted(list)
#print(list1)
total5=0
i=0
while list[i]>0:
    total5+=list[i]
    i+=1
    
print(total5)

#%%

list1=[9,8,7,6,5,4,3]
total6=0
i=0
while i<len(list1) and list1[i]>0:
    total6+=list1[i]
    i+=1
print(total6)


#%%
nytuple=('a',)# 用逗號 隔開  ， 皆視為 元組
print(type(nytuple))



