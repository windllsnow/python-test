# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:51:01 2021

@author: jason
"""

print("\n");
def hello():
    print("Hello Python!!");
    print("Hello Python!!");
    print("Hello Python!!");
    print("Hello Python!!");
hello();
hello();
hello();
#%%
def add(x001,x002):
    return x001+x002
def minus(x001,x002):
    return x001-x002
def times(x001,x002):
    return x001*x002
def dev(x001,x002):
    return x001/x002

A1=int(input("a= "));
op = int(input("想 + , - , *, /  請輸入 1 , 2 , 3, 4：  "));
A2=int(input("b= "));
if op == 1:
    print("a+b=", add(A1,A2))   # 輸出a-b字串和結果
elif op == 2:
    print("a-b=", minus(A1,A2))  
elif op == 3:
    print("a*b=", times(A1,A2))  
elif op == 4:
    print("a/b=", dev(A1,A2))      
else:
    print("運算方法輸入錯誤")
    
    #簡陋計算機 成功OK  ^  ^
#%%