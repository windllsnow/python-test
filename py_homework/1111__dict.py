# -*- coding: utf-8 -*-

x=['ans 1','ans 2','ans 3'];


a=4;
b=5;
c=6;
print(a+b+c);


print(a//b);
print("ans1=",end='');print(a%b);

x=9000;
print("x=",end='');
print(x);
print("x/b=",end='');print(x/b);



print(x%b);
print(x//b);
print (x**b);
#%%

t=11;
u=11;
z=12;
print(id(t));
print(id(u));
print(id(z));
#%%
k=divmod(z,t);
print(k);
s,t=k;
print(s);
print(t);


#%%
o=111111;
print(o);
#del o;
#print(o);
#%%
y=a+\
    b+\
        c
print(y);
                #%%
                

money =50000*(1+0.015)**5
print("本金和是",end=' ');print(money);
                #%%
PI=3.14159 ; # 把PI當作具名常數
r=5;
print("園面積=",end='  ');
area=PI*r*r;  #園面積
print(area);
cir=2*PI*r;     #圓周長
print("圓周長=",end=' ');
print(cir);
#%%
print(type(cir));
print(bin(a));
print(oct(b));
print(hex(c));

#%%
d=float(a);      #強制換 type
print(d);     


print(pow(a,b));  #a^b


e=-4889;
print(abs(e));  #絕對值

#%%

f=True;
print(type(f));
#%%

str1='''ttt tt t oasjdioogjaisjl leritj ltjiodrjstj lrsiotjos
thawet  itodjfgiodsl sdiofgih shuazip ...'''
print(str1);
print('      \     ')
str2='''fsugidsfhgui hdsfigu idskfhidsg isodfiushzigusld\
 sadhfuiashdkfuisdahfashdiufa...'''
print(str2);
#%%

'''12316516'''

kk=6.;
print (kk);
str3='''ipsfdogivdsfji123 \'456\n  58956\t 5585961  45641 56416 56154 156156\\ 1561561\"456165\' 155\
    54156891545 15654898415 5149515148...''';
print(str3);


kkl=int(area)+b; #浮點數轉整數，小數點後捨去
print(kkl);
#%%
num1=222;
num2=333;
num3=num1+num2;
print("數值相加:");
print(num3);
str5=str(num1)+str(num2);
print("強制轉換字串相加"    );
print(str5);
#%%
name1=int(input("x="));
name2=int(input("y="));
print("成續是="+str(name1+name2));
#%%
nam11=eval(input("x="));
nam22=eval(input("y="));
print(nam11+nam22);
type("nam11")
#%%

x1="a";
x2=x1*10;
print(x2);
x3="abc";
x4=x3*5;
print(x4);
#%%
x11="22";
x22="33";
x33=x11+x22;#字串相加
print(x33);
x44=int(x11)+int(x22);#轉整數&相加
print(x44);
#%%
n1=123;
n2=321;
n_sum=n1+n2;
print("相加",n_sum);# 文字+ 結果2
print("相加",end=' ');\
print(n_sum);#文字+結果2

#是一樣的表示結果

nstr1="123";
nstr2="321";
nstr_sum =nstr1+nstr2;
print("字串相加",nstr_sum);
#%%
zz=97;
xx=chr(zz);  # 97=
print(xx);
yy=ord(xx);# a=
print(yy);
xx4='鄧';
print(ord(xx4));# 輸入 '鄧' unicode 10 進位 碼值
print(hex(ord(xx4)));#輸入 '鄧' unicode 16 進位 碼值
print(oct(ord(xx4)));#輸入 '鄧' unicode 8 進位 碼值
print(bin(ord(xx4)));#輸入 '鄧' unicode 2 進位 碼值
#%%

number11=input('請輸入數字');
print(type(number11));
if(int(number11)<5):
    print('ttt');
    print('KKK');
else: 
    print("you lose ");
    
print("so so");

#%%

xxc=12*13;
xx1=1080*6*20;
xx2=(10.5)*15;
if (xxc>xx1):
    print('跳鏪');
elif(xxc>xx2):
    print('跳鏪');
else:
    print('留');
#%%
if(xxc>xx1 or xxc>xx2 ):
    print("跳 槽");
else:
    print("留");
#%%
help(print);
#%%

print("asfdf 124 gdvfidf na\n\n",end=' ',sep="$$",flush=True);
#%%
score=90;
name='SNADy';
count=1;
print("%s你的第%d次物理成績是%d" % (name,count,score));
#%%
xxx=10;
print("整數%d\n 浮點數%f\n 字串%s" % (xxx,xxx,xxx));
yyy=9.99;
print("整數%d \n 浮點數%f \n 字串%s" % (yyy,yyy,yyy));
#%%
#格式化輸出
print("x=/%6d/" % xxx);
print("yyy=/%6.2f" % yyy);
sss="deep";
print("sss=/%6s/" % sss);
print("以下是保留格數空間不足的實例");
print("x=/%2d/" % xxx); 
print("yyy=/%3.3f/" % yyy);
print("sss=/%2s/" % sss);
print("____");
print("xxx=/%-6d/" % xxx);
print("yyy=/%-6.2f/"% yyy);
print("sss=/%-6s/" % sss);
print("xxx=/%+6d/" % xxx);
print("yyy=/%+7.3f/" % yyy);
#%%
mix_list = ['aggie','tang',2020,607];
print(mix_list) ;
mix_list[1]='老師';
print(mix_list) ;
mix_list[:2]=[123,4324];#換多個就用[,]
print(mix_list);
#%%
print(len([1,2,3,4,5]));#串列個數
print(max([1,2,3,4,5]));
print(min([1,2,3,4,5]));
print(sum([1,2,3,4,5]));
print([1,2]+[3,4,5]);
print(['hello world']*3);
print(33 in [11,22,33]);#成員運算，true false
#%%
num_str=[];
print('串列有-',num_str);
num_str.append('1');
print('串列有-',num_str);
num_str.append('2');
print('串列有-',num_str);
num_str.append('3');
print('串列有-',num_str);
num_str.append('4');
print('串列有-',num_str);
num_str.insert(2,'5');#注意只能(__取第幾個__,插入字串)這種模式
print('串列有-',num_str);
num_str.pop();
print('串列有-',num_str);
num_str.pop(3);
print('串列有-',num_str);
num_str.remove('5');#remove list 裡特定字元 ,這裡刪5這數字
print('串列有-',num_str);
#%%
help(num_str.insert);#help的一種模式
#%%
"""help('sys')
help('str')
>>>a = [1,2,3]
>>>help(a)
這時help(a)則會打開list的操作方法
>>>help(a.append)
會顯示list的append方法的幫助"""
#%%
num_str.append('3');
num_str.append('58');
num_str.append('81');
num_str.append('4');
print('串列有-',num_str);

num_str.reverse();
print("新的字串的內容",num_str);

sorted_num=sorted(num_str);#小到大排序後
print("排序後",sorted_num);

sorted_num1=sorted(sorted_num,reverse=True);#大到小排序後
print("排序後2",sorted_num1);


unsorted_cars=["toyota","honda","bmw","ford","audi"];
sorted_cars=sorted(unsorted_cars);
print("原先",unsorted_cars);
print("排序後",sorted_cars);

#%%







'''
看jypter  範例
index()
索引值 = 串列名稱.index（搜尋值）
count()
次數 =串列名稱.count（搜尋值）
copy()
賦值 b=a
拷貝. b=a. copy()

sort()
串列名稱.sort() 
注意：會改掉原本的串列
排序由小到大排序
name_list.sort()
排序由大到小排序
name_list.sort(reverse=True)

join() 連接字串.join(串列) /將列表中的所有元素組合成字符串
split() /
/將字串以空格或其他符號為分隔，將字串拆開，變成串列

startswith() 字串.startswith(字串) /列出字串起始文字是否是指定子字串
endswith() 字串.endswith(字串) /列出字串結束文字是否是指定子字串
replace() replace(ch1,ch2)   /將ch1字串由ch2取代

'''

'''
for()
range()
while

break continue else

'''
#%%

for i in[1,2,3,4,5]:
    print(i)
print("\n");#換行
for j in range(1,4):
    print(j)

'''
range(start, stop[, step])
■ start 引數預設為0，step 引數預設為1
'''

print(list(range(11)));
print(list(range(2,11)));
print(list(range(2,11,2)));


#%%
msg1="你好，我是小成，跟我聊天吧，我會重複你的話~~";
msg2="輸入q離開喔";
msg=msg1+'\n'+msg2+'\n'+':';
input_msg= "#預設空字串";
while(input_msg!='q'):
    input_msg=input(msg);
    print(input_msg);#注意 q 還是會 output 完 才結束
    #%%
    
'''
for var1 in 可迭代物件： #外層 for 迴圈
   …
  for var2 in 可迭代物件： #內層 for 迴圈
        …
'''


for i in range (1,10):
    for j in range(1,10):
        result =i*j;
        #print(i,"*",j,"=",result)
        print("%d*%d=%-6d"%(i,j,result),end='');#=%-6d 等號後6格且靠左
        #%%
print("\n");     
scores=[3,38,29,49,33,42,70,78,66,78];
scores.sort(reverse=True);
print(scores);
count=0;
for sc in scores:
    count+=1
    print(sc,end="  ")
    if count==6:#到6個停 印出0~5個
        break;
#%%
        
print("\n");
scores1=[11,22,33,44,55,66,77,88,99,999,8889];
count=0;##超重要，勿忘打
for sc in scores1:
    if sc < 90 :
        continue
    count+=1
print ("成績大於90分的人數是",count,"人");
#%%

scores3 = [94,78,92,55,88,79,90,84,66,78]
for sc in scores3:
    if sc < 60:
        print("有成績小於60分的人")    
        break
else: 
  print("大家都有及格") 

print("\n");

#%%
'''
i=0
int  scores3[i]
while ( scores3[i] < 60): 不符合()裡面就跳出迴圈了'
    print("有成績小於60分的人")   
   i+=1
   
else: 
  print("大家都有及格")
 

 '''
#%%
tup1 = ('aggie', 'tang', 2020, 607)
print('更新前的tup')
for i in tup1:
    print(i)
#print([i for i in tup1])
tup1 = ('agge', 'tag', 3, 4, 5 )
print('更新後的tup')
for i in tup1:
    print(i)

#名稱一樣，直接覆寫掉


#%%
employee_dic = {13:'王小明',35:'張美麗', 200:'李大'}
salary_dic = {13:36000,35:38000, 200:40000}
print("員工id是013的人是",employee_dic[13])
print(employee_dic[13],"的薪水是",salary_dic[13])

print("\n");

employee_dic = {'013':'王小明','035':'張美麗', '200':'李大'}
salary_dic = {'013':36000,'035':38000, '200':40000}
print("員工id是013的人是",employee_dic['013'])
print(employee_dic['013'],"的薪水是",salary_dic['013'])


print("\n");

#鍵值  可用字串 元祖 數值 id()

#%%
employee_dic = {'013':'王小明','035':'張美麗', '200':'李大'}
salary_dic = {'013':36000,'035':38000, '200':40000}

employee_dic['201'] ='章筱' 
salary_dic['201'] = 27500
print("員工id是201的人是",employee_dic['201'])
print(employee_dic['201'],"的薪水是",salary_dic['201'])
print(employee_dic)
print(salary_dic)
print("\n");


employee_dic['035'] ='陳一' 
salary_dic['035'] = 28000
print("員工id號碼035改成",employee_dic['035'])
print(employee_dic['035'],"的薪水是",salary_dic['035'])
print(employee_dic)
print(salary_dic)

#%%
##上面重打


key= input("要查詢的員工id=")
if key in employee_dic:
    print ("員工id%s已經在名單裡了" % key)
    print("名字是%s" % employee_dic[key])
    print("薪水是%d" % salary_dic[key])
    
print("\n");



#%%

del employee_dic['035'];
print(employee_dic);

objkey='013';
value=employee_dic.pop(objkey);
print(employee_dic);
#%%
employee_dic = {'013':'王小明','035':'張美麗', '200':'李大'}
salary_dic = {'013':36000,'035':38000, '200':40000}
key= input ("要查詢的員工id=")
if key in employee_dic:
    print("員工id %s 在名單裡" % key)
    print("名字是 %s " % employee_dic[key])
else:
    print("員工 id %s 不在名單裡"  % key )
    value = input ("來建立他的資料，名單是？")
    employee_dic[key]=value
    print("資料已經建好了，請確認")
    print(employee_dic)


key2= input ("要查詢的員工id2=")
if key2 in salary_dic:
    print("員工id %s 在名單裡" % key2)
    print("薪水是 %s " % salary_dic[key2])
else:
    print("員工 id %s 不在名單裡"  % key2 )
    value2 = input ("來建立他的資料，名單是？")
    salary_dic[key2]=value2
    print("資料已經建好了，請確認")
    print(salary_dic)
#%%


employee_dic3 = {'013':'王小明','035':'張美麗', '200':'李大'}
ret_value1 = employee_dic3.get('001')
print(ret_value1) #沒有值，傳回預設None(<-這個單字)
ret_value2 = employee_dic3.get('001',"沒有此id")
print(ret_value2) 

#%%
employee_info={} #鍵：姓名，值：部門
employee_dic4 = {'013':'王小明','035':'張美麗', '200':'李大'}
for ids, names in employee_dic4.items():#抓上面的
    print("請輸入",names,"的部門：")#把上面的names, 抓來當下面的 ids
    employee_info[names]=input()#把key的____, 抓來當下面的 names 
    print(employee_info)#印出來

#%%























