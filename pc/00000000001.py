# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 22:34:40 2021

@author: jason
"""

#補trying


#%%
xy1=float(input("請使用者輸入土地的長度(m)= \t "));
print("使用者的土地的長度(m)=%f m \t" % xy1);
xy2=float(input("請使用者輸入土地的寬度(m)= \t "));
print("使用者的土地的寬度(m)=%f m \t" % xy2);
xy3=str(input("使用者名字= \t  "));
print("使用者的名字是 \t %s  \t" % xy3);
op1=int(input("先生,請輸入 1 ,\t, 小姐,請輸入 2 = \t "));
if op1 == 1:
    print("假設土地為正方形");  
    print("%s 先生，你的土地的總面績為: \t %.4f 坪  " % (xy3,xy1*xy2*0.3025))  
elif op1 == 2:
    print("假設土地為正方形");  
    print("%s 小姐，你的土地的總面績為: \t %.4f 坪  " % (xy3,xy1*xy2*0.3025))

