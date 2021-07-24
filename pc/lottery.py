# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:58:50 2021
@author: jason
"""

import random
lotterys=random.sample(range(1,51),7)
specialNum=lotterys.pop()
print("第xxx期的大樂透號碼",end=" \t")
for lottery in sorted(lotterys):
    print (lottery,end="  ")
print("\n 特別號:%d " % specialNum)