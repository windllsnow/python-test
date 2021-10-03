# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 20:22:27 2021

@author: jason
"""
xyz1=eval(input("請使用者輸入土地的長度(m)= \t "));
print("使用者的土地的長度(m)={} m \t".format(xyz1));
xyz2=eval(input("請使用者輸入土地的寬度(m)= \t "));
print("使用者的土地的寬度(m)={}m \t".format(xyz2));
xyz3=str(input("使用者名字= \t  "));
print("使用者的名字是 %s   \t" % xyz3);
op1=eval(input("先生,請輸入 1 ,\t, 小姐,請輸入 2 = \t "));
while(bool(op1!=1  and op1!=2)):
    op1=eval(input("先生,請輸入 1 ,\t, 小姐,請輸入 2 = \t "));

    
   

  

   
if op1 == 1:
        print("假設土地為正方形");  
        print("%s 先生，你的土地的總面績為: \t %.4f 坪  " % (xyz3,xyz1*xyz2*0.3025))  
elif op1 == 2:
        print("假設土地為正方形");  
        print("%s 小姐，你的土地的總面績為: \t %.4f 坪  " % (xyz3,xyz1*xyz2*0.3025))