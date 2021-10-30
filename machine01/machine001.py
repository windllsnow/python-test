#%%





# %%

# %%

# %%
#

# 微積分 
# #ch2
#極限
import matplotlib.pyplot as plt
from sympy.utilities.exceptions import SymPyDeprecationWarning
alchol=58
for x in range(0,11):
    if x>0:
        alchol*=0.5
    print(f"當x={x:2d},酒精濃度={alchol}")



# %%
import matplotlib.pyplot as plt
alchol=58
x=[x for x in range(0,11)]
y=[alchol*(1/2)**y for y in x]
plt.axis([0,12,0,60])               #x軸L0-12;y軸0=60
plt.plot(x,y)
plt.xlabel("Times")
plt.ylabel("Alcohol concentration")
plt.grid()                              #網格
plt.show()
# %%
import matplotlib.pyplot as plt
x=[x for x in range(1,101)]
y=[1/y for y in x]
plt.axis([0,100,0,2])
plt.plot(x,y)
plt.xlabel("n")
plt.ylabel("y")
plt.grid()
plt.show()

# %%
import  matplotlib.pyplot as plt 
import numpy as np
x=np.linspace(1,0.01,101)   #在 1~0.01 (向左)   創造 101 個點
y=[1/y for y in x]          # x 越大 ->y   正無限大
plt.axis([0,1,0,101])
plt.plot(x,y)
plt.plot(x[100],y[100],'-o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
# %%
import matplotlib.pyplot as plt 
import numpy as np
x=np.linspace(-1,-0.01,101)  #在 -1  ~ -0.01 (向右)   創造 101 個點
y=[1/y for y in x   ]       # x 越大 ->y   負無限大
plt.axis([-1,1,-101,101])
plt.plot(x,y)
plt.plot(x[100],y[100],'-o')
plt.xlabel("x")
plt.ylabel('y')
plt.grid()
plt.show()

# %%
from sympy import*
x=Symbol('x')
f=58*(1/2)**x
print("result=",limit(f,x,float("inf")))
print("result=",limit(f,x,oo))  #oo  無限


# %%
from sympy import*
x=Symbol('x')   # 宣告 x 為 變數x
f=1/x
print("右邊趨近0=",limit(f,x,0))
print("左邊趨近0=",limit(f,x,0,dir='-'))



# %%

#ch3 斜率



# %%
import matplotlib.pyplot as plt 
import numpy as np 

x=np.linspace(-5,5,101)
y=[y*y for y in x ]
plt.axis([-5,5,0,30])
plt.plot(x,y)
plt.xticks(range(-5,6,1))  #改 x軸 組成
plt.xlabel("x")
plt.ylabel('y')
plt.grid()
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-2,2,101)
y=[y *y  for y  in x ]
plt.axis([-2,2,0,4])
plt.plot(x,y)
plt.plot([1,2],[1,4],'-o')   # x 1 和 2 ; y  1 和 4   (1,1)(2,4)
plt.xticks(range(-2,3,1))
plt.text(1-0.15,1+0.1 ,'A')   # 文字顯示 位置
plt.text(2-0.15,4-0.15, "B")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

# %%



#ch4 微分

# %%
import  matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-0.01,-5,100)   #左下
y=[1/y for y in x ]  
plt.plot(x,y)

x=np.linspace(0.01,5,100)# 右上
y=[1/y for y in x ]
plt.plot(x,y)

plt.axis([-5,5,-5,5])
plt.xticks(range(-5,6,1))
plt.yticks(range(-5,6,1))
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

# %%
#ch5 微分
#%%
import matplotlib.pyplot as plt
import numpy as np 
a=3
b=-12
c=10

x_min=12/6   # 直接 用 微分 公式 得知
y_min=a*x_min**2 + b*x_min +c
plt.text(x_min-0.7,y_min+0.5,'('+str((x_min))+','+str(y_min)+")")  # 顯示 座 標
plt.plot(x_min,y_min,'-o',color='r') # 紅點


print(f"極小值x 座 標={x_min}")
print(f"極小值 y 座標{y_min}")


x=np.linspace(0,4,50)
y=a*x**2+b*x+c
plt.plot(x,y,color='b')

x_tangent=np.linspace(0,4,50)
y_tangent=[y_min for element in x_tangent] # y_min =-2  ;跑 50 個點;  等於 y=-2
plt.plot(x_tangent,y_tangent,color="g")
plt.show()



# %%
import matplotlib.pyplot as plt 
import numpy as np
a=-3
b=12
c=-9

x_max=12/6

y_max=a*x_max**2+b*x_max +c
plt.text(x_max-0.5,y_max-0.97,'('+str(x_max) +","+str(y_max)+")")
plt.plot(x_max,y_max,'-o',color='r')
print(f"極大值 x 座 標={x_max}")
print(f'極大值 y 座標={y_max}')

x=np.linspace(0,4,50)
y=a*x**2+b*x+c
plt.plot(x,y,color='b')

x_tangent=np.linspace(0,4,50)
y_tangent=[y_max for element in x_tangent] # y_max =3  ;跑 50 個點;  等於 y=3
plt.plot(x_tangent,y_tangent,color="g")
plt.show()

# %%
import matplotlib.pyplot as plt 
import numpy as np
a=3
b=-12
c=10

x_min=12/6


y_min=a*x_min**2 + b*x_min +c
plt.text(x_min-0.7,y_min+0.5,'('+str((x_min))+','+str(y_min)+")")  # 顯示 座 標
plt.plot(x_min,y_min,'-o',color='r') # 紅點

x=np.linspace(0,4,50)
y=a*x**2+b*x+c
plt.plot(x,y,color='b')


a_de=6
b_de=-12
x_de=np.linspace(0,4,50)
y_de=a_de*x+b_de
plt.plot(x_de,y_de,color='g')

x_zero=12/6
y_zero=0.0
plt.text(x_zero-0.5,y_zero+1.2,"("+str(x_zero)+","+str(y_zero)+")")
plt.plot(x_zero,y_zero,'-o',color='r')

plt.grid()
plt.show()

# %%
#繪製二次函數與切線

import matplotlib.pyplot as plt
import numpy as np
a=3
b=-12
c=10
x=np.linspace(0,5,101)
y=a*x**2+b*x+c
plt.plot(x,y,color='r')

for x_loc in range(0,5):
    y_loc=a*x_loc**2+b*x_loc+c
    slope=6*x_loc-12
    x_new=[x_loc-1,x_loc,x_loc+1]
    y_new=[slope*(x-x_loc)+y_loc for x in x_new]
    plt.plot(x_new,y_new,color='g')
plt.grid()
plt.show()

# %%


import matplotlib.pyplot as plt
import numpy as np
a=3
b=-12
c=10
x=np.linspace(0,5,101)
y=a*x**2+b*x+c
plt.plot(x,y,color='r')

for x_loc in range(0,5):
    y_loc=a*x_loc**2+b*x_loc+c
    slope=6*x_loc-12
    x_new=[x_loc-1,x_loc,x_loc+1]
    y_new=[slope*(x-x_loc)+y_loc for x in x_new]
    plt.plot(x_new,y_new,color='g')
plt.grid()
plt.axis('equal')
plt.show()



# %%

import matplotlib.pyplot as plt

a = 3
b = -12
c = 10           

# 繪製經過 x = 0-4 的40條切線
for counter in range(0, 41):
    x_loc = counter / 10
    y_loc = a*x_loc**2 + b*x_loc + c        # y座標
    slope = 6 * x_loc - 12                  # 每一點的斜率
# x_new和y_new是經過切線的座標, 只取3點連線
    x_new = [x_loc-1, x_loc, x_loc+1]
    y_new = [slope * (x - x_loc) + y_loc for x in x_new]
    plt.plot(x_new, y_new, color='g')
plt.grid()
#plt.axis('equal')                          # ch5_5_1.py此#符號取消
plt.show()



# %%
import matplotlib.pyplot as plt 
a=3
b=-12
c=10 

for counter in range(0,41):
    x_loc=counter/10
    y_loc=a*x_loc**2+b*x_loc+c
    slope=6*x_loc-12

    x_new=[x_loc-1,x_loc,x_loc+1]
    y_new=[slope*(x-x_loc)+y_loc for x in x_new]
    plt.plot(x_new,y_new,color='g')
plt.grid()
plt.axis('equal')
plt.show()
# %%
import matplotlib.pyplot as plt 
import numpy  as np
a=-1
b=50                  #area=x*(50-x)=-x2+50x

x_max=50/2
y_max=-x_max**2+50*x_max
plt.text(x_max-5,y_max-5, '('+str((x_max))+','+str(y_max)+')') 
plt.plot(x_max, y_max, '-o', color='r')     

x=np.linspace(0,51,50)
y=a*x**2+b*x

plt.plot(x,y,color='b')
plt.grid()
plt.show()


#%%

import matplotlib.pyplot as plt
import numpy as np

# 二次函數的係數
a = -3.5
b = 18.5
c = -5            

# 標記業績點
x1 = 1
y1 = 10
plt.text(x1+0.05, y1-1, '('+str((x1))+','+str(y1)+')') 
plt.plot(x1, y1, '-o', color='g')
x2 = 2
y2 = 18
plt.text(x2+0.05, y2-1, '('+str((x2))+','+str(y2)+')') 
plt.plot(x2, y2, '-o', color='g')
x3 = 3
y3 = 19
plt.text(x3+0.05, y3+0.1, '('+str((x3))+','+str(y3)+')') 
plt.plot(x3, y3, '-o', color='g')

# 繪製此函數圖形
x = np.linspace(0, 4, 50)
y = a*x**2 + b*x + c
plt.plot(x, y, color='b')

plt.grid()
plt.show()

# %%
# y=f(x)=-3.5x2+18.5x-5
import matplotlib.pyplot as plt
import numpy as np

# 二次函數的係數
a = -3.5
b = 18.5
c = -5            

# 標記業績點
x1 = 1
y1 = 10
plt.text(x1+0.05, y1-1, '('+str((x1))+','+str(y1)+')') 
plt.plot(x1, y1, '-o', color='g')
x2 = 2
y2 = 18
plt.text(x2+0.05, y2-2, '('+str((x2))+','+str(y2)+')') 
plt.plot(x2, y2, '-o', color='g')
x3 = 3
y3 = 19
plt.text(x3+0.05, y3+0.1, '('+str((x3))+','+str(y3)+')') 
plt.plot(x3, y3, '-o', color='g')

a_coe=7
b_coe=18.5
x_max=round((b_coe/a_coe),2)
y_max=round((a*x_max**2+b*x_max+c),)

plt.text(x_max-0.4, y_max-1.5, '('+str((x_max))+','+str(y_max)+')') 
plt.plot(x_max, y_max, '-o', color='r')


x = np.linspace(0, 4, 50)
y = a*x**2 + b*x + c
plt.plot(x, y, color='b')

plt.grid()
plt.show()


# %%
import matplotlib.pyplot as plt 
import numpy as np
a=1

x=np.linspace(-2,2,100)
y=a*x**3
plt.plot(x,y,color='b')
plt.plot(0,0,'-o',color='r')
plt.axis([-3,3,-10,10])
plt.grid()
plt.show()



# %%
# f(x)=3x2+2x=10
from sympy import*
x=Symbol('x')
f=Symbol('f')
f=3*x**2+2*x+10
print("f'(x)= ",f.diff())
print("f'(x)=",diff(f,x))  #解微分
print("f''(x)=",diff(f,x,2)) #微二次   函式，變數，幾次

# %%
# ch6

#%%

import matplotlib.pyplot as plt
import numpy as np

# 原始函數F(x)的係數
a = 0.5
b = 1

for C in range(-5,6,5):
    x=np.linspace(-4,4,100)
    y=a*x**2+b*x +C
    plt.plot(x,y,color='b')
    
   
plt.grid()
plt.show()

# %%
from sympy import*
x=Symbol('x')
a=Symbol('a')
f=a*x
print(integrate(f,x))  #積分


# %%
import matplotlib.pyplot as plt 
import numpy as np
a=1
b=1

x=np.linspace(0,6,100)
y=a*x+b
plt.plot(x,y,color='b')
plt.fill_between(x,y1=y,y2=0,where=(x>=1)&(x<=5),
           facecolor='lightgreen' )  #定積分
plt.grid()
plt.show()



# %%
import matplotlib.pyplot as plt
import numpy as np

a=1
x=np.linspace(0,4,1000)
y=a*x**2
plt.plot(x,y,color='b')
plt.fill_between(x,y1=y,y2=0,where=(x>=1)&(x<=3),
                    facecolor='lightgreen')
plt.grid()
plt.show()


# %%

import matplotlib.pyplot as plt
import numpy as np

c=-3
x=np.linspace(0,3,100)
y=[c for cx in x]
plt.plot(x,y,color='b')
plt.fill_between(x,y1=y,y2=0,where=(x>=0)&(x<=3),
                    facecolor='lightgreen')
plt.grid()
plt.show()


# %%
import matplotlib.pyplot as plt
import numpy as np

a=1
x=np.linspace(-3,3,1000)
y=a*x
plt.plot(x,y,color='b')
plt.fill_between(x,y1=y,y2=0,where=(x>=0)&(x<=2),
                    facecolor='lightgreen')
plt.fill_between(x,y1=y,y2=0,where=(x<=0)&(x>=-2),
                    facecolor='lightblue')

                    #正 負 分開 算
plt.grid()
plt.show()


# %%
import matplotlib.pyplot as plt
import numpy as np

# 原始函數F(x)的係數
a = -1

# 繪製此函數積分區間圖形
x = np.linspace(0, 3, 1000)
y = -a*x
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=0)&(x<=1),
                 facecolor='lightgreen')

x = np.linspace(-3, 0, 1000)
y = a*x
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=-1)&(x<=0),
                 facecolor='lightblue')

plt.grid()
plt.show()



# %%
import matplotlib.pyplot as plt
import numpy as np

a=-1
b=2

x=np.linspace(-2,5,1000)
y=a*x**2+b*x
plt.plot(x,y,color='b')
plt.fill_between(x,y1=y,y2=0,where=(x>=-2)&(x<=4),
                    facecolor='lightgreen')
plt.grid()
plt.show()



from sympy import*
x=Symbol('x')
f=-(x**2)+2*x
f1=x**2-2*x
sec1=(integrate(f1,(x,-2,0)))   # 負負得正     (l函式，(變數，積分起點，積分終點)
sec2=(integrate(f,(x,0,2)))    # 正
sec3=(integrate(f1,(x,2,4)))        # 負負得正
print(sec1)
print(sec2)
print(sec3)
print(sec1+sec2+sec3)
# %%



# %%
# ch6_8.py
import matplotlib.pyplot as plt
import numpy as np

# 原始函數F(x)的係數
a = -1
b = 2

# 繪製此函數積分區間圖形
x = np.linspace(-2, 0, 1000)
y = -a*x**2 - b*x
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=-2)&(x<=0),
                 facecolor='lightblue')

x = np.linspace(0, 2, 1000)
y = a*x**2 + b*x
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=0)&(x<=2),
                 facecolor='lightgreen')

x = np.linspace(2, 4, 1000)
y = -a*x**2 - b*x
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=2)&(x<=4),
                 facecolor='lightblue')

plt.grid()
plt.show()




# %%



# %%



# %%



# %%



# %%



# %%



# %%




