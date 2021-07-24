# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:13:51 2021

@author: jason
"""

Height=eval(input("請輸入身高(m): \t "));


while(Height > 3 or Height <  1):# 想設1~3區間的浮點數&有理數，太難，一直失敗
    print("注意單位,重key 喔");

    Height=eval(input("請輸入身高*****(m)*****: \t"));




print("身高(m):={} m \t".format(Height));
Weight=eval(input("請輸入體重(kg): \t "));
print("體重(kg):={} m \t".format(Weight));
print("\n");


bmi=float (Weight/Height**2);
if bmi >=25.5:
    print("bmi= %10.4f " % bmi)
    print("過重囉~~會被殺掉喔~");
elif bmi >=18.5:
    print("bmi= %10.4f " % bmi)
    print("正常,繼續保持喔~~");
else:
    print("bmi= %10.4f " % bmi)
    print("過輕,多吃點喔~~不然會gg喔~~");