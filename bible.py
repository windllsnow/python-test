#%%
from typing import FrozenSet
from typing_extensions import runtime


name='林小明'
score=80
name1='David'
print("{}的成績為{}".format(name,score))
print(f"{name1} 的成績為{score}")
print(f"{name1.upper()}的成績為{score}")



# %%

score3=input("請輸入數學成續")
print(f'數字成績為{score3}')

# %%
nat=input('請輸入國文成績')
math=input('請輸入數學成績')
eng=input('請輸入英文成績')
sum=int(nat)+int(math)+int(eng)
avg=sum/3
print('成績總分: %d ，平均成績: % 5.2f' %(sum,avg))
print(f"成績總分:{sum:10d},平均成績:{avg:15.2f}")


# %% 
pw=input('請輸入密碼:')
while pw !='1234':
    print("密碼錯誤！\n")
    pw=input('請輸入密碼:')
    
print("正確，歡迎光臨！\n")


# %%

score4=[65,34,74]
print(f"國文：{score4[0]}\n英文：{score4[1]}\n數學：{score4[2]}\n")


# %%
r1=range(5)
print(list(r1))
r2=range(8,0,-1)
print(list(r2))
r3=range(-1,-8,-1)
print(list(r3))


# %%
for i in range(1,11):
    print(i)
#%%
sum=0
n=int(input('請輸入正整數:'))
for i in range(1,n+1):
    sum+=i
print(f'1到 {n:10d}的整數和為{sum:10d}')

# %%
for i in range(1,10):
    for j in range(1,10):
        pp=i*j
        print(f"{i:3d}*{j:2d}={pp:-2d}",end="")
    print()

# %%
s=int(input('j='))
for i in range(1,s):
    if(i==s):
        break
    print(i,end=",  ")

# %%

k=int(input("請輸入樓層:"))
print("本大樓的樓層:")
if(k>3):

    k+=1
for i in range(1,k+1):
    if( i== 4):
        continue
    print(i,end=" ")
print()

#%%
a=int(input("請輸入大於1的整數:"))
while a  in range(-100000,2):
    print("MD,看清楚哦!!!=重輸啦!!")
    a=int(input("請輸入大於1的整數:")) 
if a==2:
    print("2是質數")
    
for j in range(2,a):#  不能放a+1 哦
    if a%j==0:
        print(f"{a}不是質數",end="\n")
        break
    else:
        print(f"{a}是質數")
       
# %%
total0=n1=0
while(n1<10):
    n1+=1
    total0+=n1
print(total0)
#%%
a1=eval(input("人數:")) #若 2
total1=score5=0
person=0
while(person<=a1-1):# 0 1 ，2跳出去，2筆資料
    person+=1
    total1+=score5
    score5=eval(input(f"請輸入第{person:5d}的成績"))
average=float(score5/person)
print(f"全部的總分的{score5:-8.2f}平均為{average:-8.2f} ")# 記得沒%

# %%
list1=[0,1,2,3,4,5,6,7,8,9]
print(list1)
list1.append(10)
print(list1)
list1.insert(0,77)#前:位置，後:元素
print(list1)
list1.append([44,55])#list & 元素  都可
print(list1)
list1.extend([99,101])# 只能是list 哦
print(list1)
p1=list1.pop()
print(p1)
print(list1)
p2=list1.pop(3)
print(p2)
print(list1)
# %%
scroe6=[]
total3=inscore=0
while (inscore != -1):
    inscore= int(input('請輸入學生的成績'))
    scroe6.append(inscore)
    
scroe6.pop()

print(f"共有{len(scroe6):5d}學生")
for i in range (0,len(scroe6)):
    total3+=scroe6[i]
average1=total3/len(scroe6)
print(f"本機的總成績{total3:2.2f}，平均成績{average1:2.2f}")
# %%
students=int(input("學生人數:"))#cp
scroe6=[]
total3=inscore=0
jj=0#cp
while (jj <=students-1):#cp
    inscore= int(input(f'請輸入學生{jj+1:2d}的成績'))#cp
    jj+=1#cp
    scroe6.append(inscore)
print(f"共有{len(scroe6):5d}學生")
for i in range (0,len(scroe6)):# cp
    total3+=scroe6[i]
average1=total3/len(scroe6)#cp
print(f"本機的總成績{total3:2.2f}，平均成績{average1:2.2f}")
# %%
tuple1=(1,2,3,4,5)
tuple2=(1,"香蕉",[1,2],True)
print(tuple1)
print(tuple2)
# 不能改 讀取快
# %%

#tuple2=tuple(list1)
#list2=list(tuple1)

# %%
dict1={'香蕉':20,'蘋果':50,'橘子':30}
dict2=dict([['香蕉',21],['蘋果',51],['橘子',31],['橘子',4444]])
print(dict1)
print(dict2)
print(dict1['蘋果'])
print(dict2['橘子'])#只抓最後值  前面(鍵-值) 被覆蓋
print(dict1.get('芒果'))
print(dict1.get('芒果',100001))
print(dict['芒果'])
# %%
dict3={'A':'內向','B':'外向','O':'和善','AB':'分裂者',\

'a':'內向','b':'外向','o':'和善','ab':'分裂者'}
aaa=input('請輸入血型(A,B,AB,O):')
blood=dict3.get(aaa)
if blood == None:
    print('沒有「    '+  aaa +'」血型  ')
else:
    print('你的血型是「'+ aaa +'」型')

#%%


dict2=dict([['香蕉',21],['蘋果',51],['橘子',31],['橘子',4444]])
print(dict2)
dict2["橘子"]=60
print(dict2)
dict2['鳳梨']=1111
print(dict2)

print('='*44)

dict4={'香蕉':20,'蘋果':50,'橘子':30,'橘子':4444}
del dict4['橘子']
print(dict4)
dict4.clear()
print(dict4)
del dict4
print(dict4)
#%%

dict2=dict([['香蕉',21],['蘋果',51],['橘子',31],['橘子',4444]])

item1=dict2.items()
key1=dict2.keys()
value1=dict2.values()
nnn=dict2.setdefault('香蕉')
print(item1)#鍵-值
print(key1)#鍵
print(value1)#值
print(nnn)   #   與 get() 同
print("香蕉" in dict2)
print('lalala' in dict2)
# %%
dict5={'林小明':85,'曾山水':12,'鄭美麗':90}
name2=input("輸入人名:")
if name2 in dict5:
    print(name2 +'的成績'+str(dict5[name2]))
else:
    score7=int(input('輸入學生分數:'))
    dict5[name2]=score7
    print("字典內容："  + str(dict5))

# %%
dict4={'香蕉':20,'蘋果':50,'橘子':30,'橘子':4444}
key2=dict4.keys()
print(key2)
key2_2=list(dict4.keys())
print(key2_2[0])

print("="*40)

value2=dict4.values()
print(value2)
value2_2=list(dict4.values())
print(value2_2[0])

print("-"*40)

item2=dict4.items()
print(item2)
item2_2=list(dict4.items())
print(item2_2[1])      #2nd 鍵-值
print(item2_2[1][0])   #2nd 鍵
print(item2_2[1][1])   #2nd 值

for name00, num00 in item2_2:
    print(f"得到的 {name00:4s} 數目為 {num00:4d}面")


# %%
dict6={'香蕉':20,'蘋果':50,'橘子':30,'西瓜':404}
n01=dict6.setdefault('蘋果')         #有的
n02=dict6.setdefault('蘋果',100)    # 有的 不給改
n03=dict6.setdefault('冬瓜')        #沒有的  none
n04=dict6.setdefault('冬瓜1',41)    #沒有的  改哦!!

print(n01)
print(n02)
print(n03)
print(n04)
print(dict6)


# %%
fruits={'banana','apple','orange','banana'} # 重覆的話 只有一個
print(fruits)
print(type(fruits))

fruits01={'香蕉','banana',100,(1,2)}
print(fruits01)

fruits02={[1,2],{14:11},{1,2}} #list dict  set 不可以放集合裡
print(fruits02)
#%%
fruits03=set(['香蕉','apple','kelt',1223])
print(fruits03)
print(type(fruits03))

print('='*10)

s01=set('Goof Boy !')
print(s01)                  # 會拆掉
print(type(s01))


print('='*10)

s1={}
print(type(s1))
s2=set()
print(type(s2))
# %%
person01=['林小明','王常歐','縮縮鬥','隔壁老王','lala','你說呢','曾美麗','林小明']
s001=set(person01)
print(s001)
list2=list(s001)  # 轉list
print(list2)
print(list2[0])  # 轉list 才能讀 特定位置


# %%
'''
&交集
|聯集
-差集
^對稱差集
== 等於
!=不等於
in  是成員
not in 不長成員

'''
A={1,2,3,4,5,6,7}
B={9,8,7,6,5,4,3}
print(A&B)
print(A|B)
print(A-B)
print(A^B)
print(A==B)
print(A!=B)
print(2 in B)
print(2 not in B)

print('_'*50)


A.add('C')
# A.clear() 刪完成 空集合
# A.copy()
# A.pop()  隨機刪 ，刪 空集合 會 error

A.update(B)  #把 B 加入A
print(A)
print(B)  # 不變

print('_'*50)

A.discard(2)
print(A)
A.discard(99) # 不會跳 error
print(A)
A.remove(99)  # error
print(A)
# %%
'''
max(A)
min(A)
sum(A) #數字 才能
len(A) # 元素個數
'''
AA={1,5,7,3,9,7,3,9,3,3,9,55,66,77,88,99,1234,443,453179,100}
S_AA=sorted(AA)
S01_AA=sorted(AA,reverse=True)


print(len(AA))  #重覆的  算一個
print(AA)
print(S_AA)
print(S01_AA)

# %%
# 集合不可以 for迴 圈i
langs={'python','java','kotlin'}
enum_langs=enumerate(langs) # 轉成enumerate 物件
print(list(enum_langs))


print("="*45)

for item in enumerate(langs):  # 只能是【enumerate(langs)】 不懂??????????????
    print(item)
for i,item in enumerate(langs):
    print(i,item) 




#%%
#set  可變集合  frozenset 不可變集合  不能用add() clear() discard() pop() remove() update()
AAA=frozenset([1,2,3,4])
BBB=frozenset([4,5,6,7])

print(AAA&BBB)
print(AAA|BBB)
print(AAA-BBB)
print(AAA^BBB)
print(sum(AAA))
print(max(AAA))
# %%
c00=float(input('請輸圓半徑:'))
def Circle(radius):
    area= radius*radius*3.14
    length= 2*radius*3.14
    return area,length
c1=Circle(c00)
print(f'圓面績:{c1[0]:6.2f} ，圓周長{c1[1]:6.2f}')

# %%
#參數預設值
def getarea(width, height=12):
    return width*height
ret1= getarea(6)
ret2=getarea(6,22)
print(ret1)
print(ret2)
# %%
def scope():
    var1=1
    print(var1,var2)# 只有此函式裡 var11=1
  

var1 =10
var2= 20

scope()
print(var1,var2)

def scope1():
    global var11   # 整個python 專案 var11都=1
    var11=1
    var22=2
    print(var11,var22)

var11=10
var22=20
scope1()
print(var11,var22)





# %%

# %%

# %%

# %%
