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

#_______________數值函數____________________________
z1=abs(-5)       # 絕對值
z2=chr(65)       #取 x的字元
z3=divmod(44,6)  #x/y =(商,餘數)
z4=hex(34)       #  x 轉 16 進位
z5=oct(34)       #  x 轉 8 進位
z6=ord("我")     #  x  的 unicode 值
z7=pow(2,3)      #  (x,y)  等於 x**y
z8=round(45.8)   # 四捨六入
z9=sorted([3,1,7,5]) #由小到大
print(z1)
print(z2)
print(z3)
print(z4)
print(z5)
print(z6)
print(z7)
print(z8)
print(z9)

print("="*10)

yy1=pow(2,3,7)
print(yy1)   #2**3/7 =8/7  餘數為1


print('='*10)

ret1=divmod(44,6)
print(ret1[0],ret1[1])    
print(type(ret1))  # tuple
print(ret1)


print('='*10)

rr1=round(2.4)
rr2=round(2.6)
rr3=round(3.5)
rr4=round(4.5)
rr5=round(3.75,1)
rr6=round(4.786868,3)
print(rr1,rr2,rr3,rr4,rr5,rr6)


print('='*10)
#%%

person001=int(input("請輸入學生人數: "))
apple=int(input("請輸入蘋果總數:  "))
ret01=divmod(apple,person001)
print("每個學生可分得蘋果", str(ret01[0]),'個')
print('蘋果剩餘',str(ret01[1]),'個')

#%%

print(max(1,2,3,4))
print(max([1,2,3,4]))
print(sum([1,2,3,4]))
print(sum([1,2,3,4],10))
print(sorted([3,1,7,8])) #預設  false  由小到大排序
print(sorted([3,1,7,8],reverse=True))


#%%
innum=0
list3=[]
while (innum!= -1):
    innum=int(input("請輸入電費:  "))
    list3.append(innum)
print(list3)
list3.pop()     # list.pop() 刪預設值 ;dict.pop(key, def) 如dict.pop('a':123) or dict.pop('a')
print(f"共輸入{len(list3):5d},最多電費{max(list3):5d},最少電費{min(list3):5d},總電費{sum(list3):5d}")
print(f"電費由大到小排序為:{sorted(list3,reverse=True)} ")


# %%

#_______________字串函數____________________________
#擴充字元 要大於 原本長度 ，只能有一個字元，預設一個空白字元
z10='book'.center(8)       #(  book  )  擴充8字元 置中
z11="book".ljust(8)        #(book    )  擴充8字元 置左                         
z12="book".rjust(8)        #(    book)  擴充8字元 置右
z27='book'.center(10,"$")

#文字中間不會移除
z13=" book ".lstrip()      #(book ) 移除左邊空格
z14=" book ".rstrip()      #( book) 移除右邊空格
z15=" book ".strip()       #(book)移除左右邊空格
z28='  This  is a book  '.strip()

z16='abc'.startswith("a")  #True
z17='abc'.endswith('c')    #True

z18='#'.join(['ab','cd'])  #ab#cd
z19="ab#cd".split("#")     #['ab','cd'] 預設1個空白字元

z20='Yes'.islower()        #False
z21='YES'.isupper()        #True

z22='book'.find('k')       #3 , 不存在的話 回傳-1
z29='book'.find('a')

z23=len('book')            #4
z24="Yes".upper()          #YES
z25="YEs".lower()          #yes

z26="book".replace('o','a')#baak

str011="I love python."
print(str011.replace('o','@'))
print(str011.replace('o','@',1))
print(str011.replace('python','django'))
print("="*60)

print(z10)
print(z11)
print(z12)
print(z27)

print(z13)
print(z14)
print(z15)
print(z28)

print(z16)
print(z17)
print(z18)
print(z19)
print(z20)
print(z21)

print(z22)
print(z29)

print(z23)
print(z24)
print(z25)
print(z26)

# %%
listname=['林小明','陳阿中','張小英']
listchinese=[100,72,90]
listmath=[87,88,65]
listenglish=[79,100,9]
print("姓名   座號   國文   數學   英文")
for i  in range(0,3):
    print(listname[i].ljust(5),str(i+1).rjust(3),\
    str(listchinese[i]).rjust(5),str(listmath[i]).rjust(5),\
    str(listenglish[i]).rjust(5))



# %%

date1='2017-8-23'
date1=" 西元 "+date1
date1=date1.replace("-"," 年 ", 1)
date1=date1.replace('-'," 月 ", 1)
date1+=" 日 "
print(date1)

# %%
import random as r
str1="abcdefg"
list001=[1,23,54,1,'ab','cd','ef']
print(r.choice(str1))# 由字串中隨機一個字元
print(r.sample(str1,3))#由字串中隨機n個字元


print(r.randint(1,10))# 由n1到n2 隨機一個 整數
print(r.uniform(1,10))# 由n1到n2 隨機一個 浮點數

print(r.randrange(0,18,2))# 由n1到n2 每隔 n3 隨機一個 整數


print(r.random())     # 由0到1 隨機一個 浮點數


r.shuffle(list001) #串列洗牌
print(list001)


# %%
import random as r

while True:
    inkey=input('按任意鍵再按[Enter]鍵擲骰子，直接按[Enter]鍵結束: ')
    if len(inkey)>0:
        num123=r.randint(1,6)
        print("你擲的骰子點數: "+str(num123))
    else:
        print("遊戲結束! ")
        break


# %%

import random as r
list002=r.sample(range(1,50),7)
special=list002.pop()
list002.sort()
print("本期大樂透的中獎號碼為：",end="")

# 這迴圈重點是  ","
for i in range(0,6):
    if i ==5:
        print(str(list002[i]))
    else:
        print(str(list002[i]),end=' , ')
print("本期大樂透特別號為："+ str(special))

print(list002)
# %%

import time 
print(time.sleep(2))
print(time.time())           #目前時間數值
print(time.localtime())      # 時間元組<=(目前時間數值)
print(time.localtime(time.time()))

print("="*20)

time1=time.localtime(time.time())
print(time1.tm_year)
print(time1[0])

print("="*20)

print(time.ctime())       #時間字串<=(目前時間數值)
print(time.ctime(time.time()))



'''
0  tm_year  西元年
1  tm_mon   月  1-12
2  tm_mday  日  1-31
3  tm_hour  小時 0-23
4  tm_min   分   0-59
5  tm_sec   秒   0-60
6  tm_wday  星期機 -->0-6<--   (一~日)
7  tm_yday  一年的第幾天 1-366  
8  tm_isdst 時光節約時間 -->1/0<--  (有/無)
'''

# %%
import  time 
start=(time.time())
print(f"開始時間：{start} ")
for i in range(500):     #執行500次 每次間隔0.0001s
    time.sleep(0.001)
end=(time.time())
print(f"結束時間： {end}")
print(f"使用時間：{end-start:7.3f}")



# %%

import time as  t
week=['一','二','三','四','五','六','日']
dst=['有日光節約時間','無日光節約時間']
time2=t.localtime()
show="現在時間：中華民國"+str(int(time2.tm_year)-1911)+"年"+str(int(time2.tm_mon))+"月"\
    +str(int(time2.tm_mday))+"日"+str(int(time2.tm_hour))+"點"+str(int(time2.tm_min))+"分"\
    +str(int(time2.tm_sec))+"秒 星期"+week[time2.tm_wday]+"\n"\
    "今天是今年的第"+str(int(time2.tm_yday))+"天 ，此地"+dst[time2.tm_isdst]



print(show)




# %%
#__________________________________________物件導向__________________
# __建立類別______-
class Animal():
    name3="小鳥"
    def sing(self):
        print("很會唱歌")

bird=Animal()
print(bird.name3)
bird.sing()


# %%

class Animal1():                    #類別
    def __init__(self,name):        # 
        self.name=name              #屬性                . 屬性        
    def sing(self):                 #方法                   .方法()
        print(self.name +",很會唱歌！")
bird =Animal1("鸚鵡")               # 以Animal1 類別，建立一個名叫鸚鵡的bird 物件
print(bird.name)
bird.sing()



# %%
class Animal2():                   
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self):
        print(self.name + str(self.age) + "歲，很會唱歌！")
    def grow (self,year):
        self.age+=year


bird1=Animal2("鸚鵡",1)  #1歲
bird1.grow(2)   # 長大2歲
bird1.sing()   #1+2歲


# %%
#_________________類別封裝_______________________________

class Animal3():
    def __init__(self,name,age):
        self.__name=name   # 僅 類別 內 可用  ， 私用， 叫 封裝
        self.__age=age
    def __sing(self):
        print(self.__name+ str(self.__age),end= "歲，很會唱歌，")
    def talk(self):
        self.__sing()
        print('也會模仿人類說話！')

bird2=Animal3("灰鸚鵡",2)
bird2.talk()

bird2__age=-1     # 封裝 屬性 、方法 ， 不能改
bird2.talk()
#bird.__sing()


# %%
#_________________類別繼承_____________________________

class Animal4():
    def __init__(self,name):
        self.name=name          # 定義 共屬性
    def fly(self):              # 定義 共方法
        print(self.name+'很會飛')

class Bird(Animal4):
    def __init__(self, name):
        self.name = '粉紅色' + name   # 覆寫 父 類別的建構式
    def sing(self):
        print(self.name + ' 也愛唱歌')

pigeon=Animal4("小白鴿")
pigeon.fly()

parrot=Bird('小鸚鵡')
parrot.fly()
parrot.sing()


# %%
#  super()   單繼承  ok ；多繼承  麻煩





# %%
#________________________多型_______________________________




# %%






# %%
#______________________多重繼承________________________________





# %%

# %%

# %%

# %%

# %%

# %%
