# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:58:50 2021

@author: jason
"""

num_str=[];

num_str.append(eval(input("請輸入a隊隊員1:\t")));
num_str.append(eval(input("請輸入a隊隊員2:\t")));
num_str.append(eval(input("請輸入a隊隊員3:\t")));
num_str.append(eval(input("請輸入a隊隊員4:\t")));
num_str.append(eval(input("請輸入a隊隊員5:\t")));
print('a隊隊員有-',num_str);


num_str2=[];
num_str2.append(eval(input("請輸入b隊隊員1:\t")));
num_str2.append(eval(input("請輸入b隊隊員2:\t")));
num_str2.append(eval(input("請輸入b隊隊員3:\t")));
print('b隊隊員有-',num_str2);
kkk=set(num_str)
kkk2=set(num_str2)

if kkk.isdisjoint(kkk2):
    print("沒有一約兩簽的隊員哦~~~~");
else:
    C=kkk.intersection(kkk2)
    print(f"兩隊都有={C}" )
    kkk.difference_update(kkk2);
   
    print(f"a隊只剩有={kkk}\t")
  