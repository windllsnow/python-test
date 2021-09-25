#%%
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
print(f"共有{len(scroe6)-1:5d}學生")
for i in range (0,len(scroe6)-1):
    total3+=scroe6[i]
average1=total3/len(scroe6)-1
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



# %%

# %%

#%%



