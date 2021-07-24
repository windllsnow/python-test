# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:58:50 2021
@author: jason
"""
#%%

#輸入幾期，算最末期的本利和

a=eval(input("本金money= \t "));
b=eval(input("利率ir= \t"));
c=eval(input("幾期n= \t"));

          
earns=range(1,c+1);
print('列出本利和');
for i in earns[c-1:]:
  
    while(i<c+1):
        
        print(f'第{i}的本金和= \t {a*(1+b)**i}');
        print(f"共{c}期")    
        break;
 #%%
 #輸入幾期，列出每期的本利和

a=eval(input("本金money= \t "));
b=eval(input("利率ir= \t"));
c=eval(input("幾期n= \t"));

          
earns=range(1,c+1);
print('列出本利和');
for i in earns:
  
    while(i<c+1):
        
        print(f'第{i}的本金和= \t {a*(1+b)**i}');
        print(f"共{c}期")    
        break;
        #%%
        #輸入幾期，列出每期的本利和，大於5期請重輸入喔

a=eval(input("本金money= \t "));
b=eval(input("利率ir= \t"));
c=eval(input("幾期n= \t"));

          
earns=range(1,c);
for i in earns:
    while(c>5):
        print('列出本利和');
        print('請重新輸入喔~~');
        c=eval(input("幾期n= \t"));
        
        


for i in earns:       
    print(f'第{i}的本金和= \t {a*(1+b)**i} \n');
print(f"共{c}期\n")    
     