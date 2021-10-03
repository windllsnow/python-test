# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 06:18:15 2021

@author: jason
"""


#%%

print("請輸入兩組座標: 依序為 (x,y) (z,t)  \t :");
x= eval(input(" \n"));
y= eval(input(" \n"));
z= eval(input(" \n"));
t= eval(input(" \n"));


def mule3(x,y,z,t):
  
    z1=float(((x-z)**2)+((y-t)**2))**0.5
    
    return  z1

a=mule3(x,y,z,t);
print("你輸入的座標距離為=%5.5f" % a)