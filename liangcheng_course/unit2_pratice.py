#!/usr/bin/env python
# coding: utf-8

# In[24]:


from jupyterthemes import get_themes
from jupyterthemes.stylefx import set_nb_theme
set_nb_theme('onedork')


# In[25]:


get_ipython().system('pip install matplotlib')


# In[26]:


import matplotlib.pyplot as plt


# In[27]:


squarea=[1,4,8,17,25,30,49,64,81,99]
plt.plot(squarea)
plt.show()


# In[28]:


import matplotlib.pyplot as plt
squares=[1,4,8,17,25,30,49,64,81,99]
plt.plot(squares)

plt.axis([0,8,0,90])
plt.show()


# In[29]:


import matplotlib.pyplot as plt
squares=[1,4,8,17,25,30,49,64,81,99]

plt.plot(squares,linewidth=7)
plt.title("Demo Chart",fontsize=32)
plt.xlabel("value",fontsize=23)
plt.ylabel("Square",fontsize=20)
plt.tick_params(axis='both',labelsize=7,color='red')
plt.axis([0,10,0,90])
plt.show()


# In[30]:


import matplotlib.pyplot as plt
data1=[1,4,8,17,25,30,49,64,81]
data2=[1,2,4,6,8,10,12,14,16]
seq=[1,2,3,4,5,6,7,8,9]
plt.plot(seq,data1,seq,data2,linewidth=3)
plt.title("Demo Chart",fontsize=32)
plt.xlabel("value",fontsize=23)
plt.ylabel("Square",fontsize=20)
plt.tick_params(axis='both',labelsize=7,color='red')
plt.show()


# In[31]:


import matplotlib.pyplot as plt
data1=[1,4,8,17,25,30,49,64,81]
data2=[1,2,4,6,8,10,12,14,16]
data3=[1,6,16,26,36,46,56,66,99]
data4=[1,1,56,31,44,85,6,77,9]
seq=[1,2,3,4,5,6,7,8,9]
plt.plot(seq,data1,'g--',seq,data2,'r-.',seq,data3,'b-',seq,data4,'y-',linewidth=7)
plt.title("Demo Chart",fontsize=32)
plt.xlabel("value",fontsize=23)
plt.ylabel("Square",fontsize=20)
plt.tick_params(axis='both',labelsize=7,color='red')
plt.show()
plt.savefig('demo.png')


# In[ ]:





# In[ ]:





# In[32]:


import matplotlib.pyplot as plt
Benz = [3080, 4620, 6549] # Benz線條
BMW = [3800, 2590, 4388] # BMW線條
Lexus = [6500, 5430, 7450] # Lexus線條
seq = [2018, 2019, 2020] # 年度
plt.xticks(seq)
plt.plot(seq, Benz,'--o',label='benz')
plt.plot(seq, BMW,'-s',label='BMW')
plt.plot(seq, Lexus,'-^',label='Lexus')
plt.title("Sales Report", fontsize=24)
plt.xlabel("Year", fontsize=3)
plt.ylabel("Number of Sales", fontsize=14)
plt.legend(loc='best')
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()
plt.savefig('legend.png')


# In[ ]:





# In[33]:


import matplotlib.pyplot as plt
plt.scatter(5,5,1000,'red')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[34]:


import matplotlib.pyplot as plt
xpt=[1,2,3,4,5]
ypt=[1,4,9,16,25]
plt.scatter(xpt,ypt)
plt.show()


# In[35]:


xlst=[]
for  n in range(6):
    xlst.append(n)
print(xlst)


# In[36]:


xlst=[n for n in range(6)]
print(xlst)


# In[37]:


import matplotlib.pyplot as plt
xpt = list(range(1,101))
ypt = [x**2 for x in xpt ]# 取x裡 變平方 給y
plt.scatter(xpt, ypt,color='y')
plt.show()


# In[38]:


import matplotlib.pyplot as plt
data01=[1,4,9,16,25,36,49,64,81]
data02=[1,2,4,6,8,10,12,14,16]
seq=[1,2,3,4,5,6,7,8,9]
plt.figure(1)
plt.plot(seq,data01,'-o')
plt.figure(2)
plt.plot(seq,data02,'--s')
plt.title("Demo chart 2",fontsize=32)
plt.xlabel("x-value",fontsize=24)
plt.ylabel("y-value",fontsize=20)
plt.tick_params(axis='both',labelsize=12,color='red')# axis 是軸；axis 可选 x、y、both
plt.show()


# subplot(x1,x2,x3) 
#  x1 垂直幾張  x2 水平幾張  x3第幾張

# ![image.png](attachment:image.png)
# 
# 
# 

# In[ ]:





# In[ ]:





# In[39]:


import matplotlib.pyplot as plt 
data01=[1,4,9,16,25,36,49,64,81]
data02=[1,2,4,6,8,10,12,14,16]
seq=[1,2,3,4,5,6,7,8,9]
plt.subplot(2,1,1)
plt.subplots_adjust(hspace = 0.9  )
plt.plot(seq,data01,'-or')
plt.subplot(2,1,2)
plt.plot(seq,data02,'--sb')
plt.title("Demo chart 2",fontsize=22,loc='center')
plt.xlabel("x-value",fontsize=14)
plt.ylabel("y-value",fontsize=10)
plt.tick_params(axis='both',labelsize=8,color='red')# axis 是軸；axis 可选 x、y、both
plt.show()


# left  = 0.125  # the left side of the subplots of the figure
# right = 0.9    # the right side of the subplots of the figure
# bottom = 0.1   # the bottom of the subplots of the figure
# top = 0.9      # the top of the subplots of the figure
# wspace = 0.2   # the amount of width reserved for blank space between subplots,
#                # expressed as a fraction of the average axis width
# hspace = 0.2   # the amount of height reserved for white space between subplots,
#                # expressed as a fraction of the average axis height
# ————————————————
# 版权声明：本文为CSDN博主「GuokLiu」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_33039859/article/details/79424858

# In[40]:


get_ipython().system('pip install twstock')
get_ipython().system('pip install lxml')


# In[41]:


import twstock
stock2330= twstock.Stock("2330")
print(stock2330)


# sid 股票代號字串
# open 近31天的開盤價(元)串列
# high 近31天的最高價(元)串列
# low 近31天的最低價(元)串列
# close or price 近31天的收盤價(元)串列
# capacity 近31天的成交量(股)串列
# transaction 近31天的成交筆數(筆)串列
# turnover 近31天的成交金額(元)串列
# change 近31天的漲跌幅(元)串列
# date 近31天的交易日期datatime串列
# data 近31天的全部資料內容串列
# raw_data 近31天的原始資料串列

# In[ ]:





# In[42]:


import twstock
stock2330 = twstock.Stock("2330")
print("股票代號 : ", stock2330.sid)
print("股票收盤價 : ", stock2330.price)


# In[43]:


import matplotlib.pyplot as plt
import twstock
stock2330= twstock.Stock("2330")#先抓，再丟給它



plt.rcParams['font.family'] = 'Adobe Gothic Std'





plt.title(u"台積電",fontsize=24)
plt.plot(stock2330.price)#再丟給它，畫圖
plt.savefig('台積電.png')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[44]:


#查詢系統已安裝的中文字體
from matplotlib import font_manager
font_set = {f.name for f in
font_manager.fontManager.ttflist}
for f in font_set:
    print(f)


# In[45]:


#檢驗是否可以顯示中文
from matplotlib import pyplot as plt
plt.rcParams['font.family'] = 'Adobe Gothic Std'
plt.text(.5, .5, '台積電')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# fetch_31() 最近31天的交易資料(Data 物件)串列
# fetch(year, month) 指定年月的交易資料(Data 物件)串列
# fetch_from(year, month) 指定年月至今的交易資料(Data 物件)串列
# moving_average(data,days) 串列數據data的days日平均值串列
# continuous(data) 串列data持續上漲天數

# In[46]:


stock2330=twstock.Stock("2330")
stock2330.fetch_from(2020,6)

plt.rcParams['font.family'] = 'Adobe Gothic Std'

plt.rcParams['axes.unicode_minus']=False

plt.title(u'台積電',fontsize=23)#橫軸名稱 u"中文字串"
plt.xlabel(u"2020年3月以來的交易天數",fontsize=13)
plt.ylabel(u"價格",fontsize=15)
plt.plot(stock2330.price)
plt.show()


# <font color=#663399 size=25 face=雅黑>day2__CSV</font>
# 
# 
# 
# 
# 

# In[47]:


import csv


# with open(檔案名稱) as csvFile     #csvFile自己命名的檔案名
# 或
# csvFile =open(檔案名案)

# In[48]:


import csv
fn='py_six/day2-20210724T050933Z-001/day2/csvReport.csv'
with open(fn) as csvFile:
    csvReader=csv.reader(csvFile)#讀檔案建立Reader物件
    listReader=list (csvReader)#將資料轉成串列
print(listReader)


# In[49]:


import csv
fn='py_six/day2-20210724T050933Z-001/day2/csvReport.csv'
with open(fn) as csvFile:
    csvReader=csv.reader(csvFile)#讀檔案建立Reader物件
    for row in csvReader:#用迴圈列出csvReader物件內容
        print("Row %s = " % csvReader.line_num,row)


# In[50]:


import csv
fn='py_six/day2-20210724T050933Z-001/day2/csvReport.csv'
with open(fn) as csvFile:
    csvReader=csv.reader(csvFile)#讀檔案建立Reader物件
    listReport= list(csvReader)#將資料轉成串列
    for row in listReport:#使用迴圈列出串列內容
        print(row)


# In[51]:


import csv
fn='py_six/day2-20210724T050933Z-001/day2/csvReport.csv'
with open(fn) as csvFile:
    csvReader=csv.reader(csvFile)#讀檔案建立Reader物件
    listReport= list(csvReader)#將資料轉成串列
print(listReport[0][1],listReport[0][5])#第？列第？個
print(listReport[1][5],listReport[1][3])
print(listReport[2][5],listReport[2][6])


# In[52]:


import csv
fn='py_six/day2-20210724T050933Z-001/day2/csvPeople.csv'
with open(fn) as csvFile:
    csvDictReader=csv.DictReader(csvFile)#讀檔案建立DictReader物件
    for row in csvDictReader:
        print(row)


# In[ ]:





# In[53]:


import csv
fn='py_six/day2-20210724T050933Z-001/day2/csvPeople.csv'
with open(fn) as csvFile:
    csvDictReader=csv.DictReader(csvFile)#讀檔案建立DictReader物件
    for row in csvDictReader:
        print(row['first_name'],row['last_name'])


# 寫入CSV檔案
# 
# 使用writer物件
# with open(‘檔案名稱’,’w’) as csvFile:
# outWriter = csv.writer(csvFile)

# In[54]:


import csv
fn='py_six/day2-20210724T050933Z-001/day2/writerow.csv'
with open(fn,'w') as csvFile:
    csvWriter=csv.writer(csvFile,delimiter='\t')#建立Writer物件
    #資料寫入CSV檔時,預設的分隔符號是逗號,
    #用delimiter更改分隔符號
    csvWriter.writerow(['Name','Age','City'])
    csvWriter.writerow(['Tang','35','taipei'])
    csvWriter.writerow(['Aggie','40','San Francisco'])

    


# In[55]:


import csv
fn='py_six/day2-20210724T050933Z-001/day2/writedict.csv'
with open(fn,'w') as csvFile:
    fields=['Name','Age','City']
    dictWriter = csv.DictWriter(csvFile,fieldnames=fields)
    dictWriter.writeheader()#寫入標題
    dictWriter.writerow({'Name':'Tanf','Age':'35','City':'Taipei'})
    dictWriter.writerow({'Name':'Aggie','Age':'40','City':'San Francisco'})



# In[56]:


import csv
dictList=[{'Name':'Tanf','Age':'35','City':'Taipei'},{'Name':'Aggie','Age':'40','City':'San Francisco'}]
fn='py_six/day2-20210724T050933Z-001/day2/write_dictlist.csv'
with open(fn,'w') as csvFile:
    fields=['Name','Age','City']
    dictWriter = csv.DictWriter(csvFile,fieldnames=fields)
    dictWriter.writeheader()#寫入標題
    for row in dictList:
        dictWriter.writerow(row)


# 瀏覽器跟網站之間的交換資料,只能文字交換
# JSON全名JavaScript Object Notation,可知最初
# 是由JavaScript開發的
# 流程是將JavaScript物件轉換成JSON,將JSON
# 傳送到伺服器,並從伺服器接收JSON,將JSON轉
# 換成JavaScript物件
# 
# JSON的兩種資料格式
# ■ 物件(object):一般用大括號{ }表示
# ■ 陣列(array):一般用中括號[]表示
# 
# <font color=#663300 size=6 >json格式中字串需用雙引號,文件裡不可以有註解</font>
# 
# -物件(object)
# 例如:
# {“Name”:“Aggie”, “Age”:25}
# # {鍵:值} 鍵要是文字
# 
# -陣列(array)
# 陣列是由一系列的值(value)所組成,由左中括號“[”
# 開始,右中括號“]”鍵結束
# 
# 

# 使用json.dump()模組
# 
# 
# 
# python資料__JSON資料<br>
# dict _____________object<br>
# list, tuple ______array<br>
# str, unicode______string<br>
# int, float, long__number<br>
# True______________true<br>
# False_____________false<br>
# None______________null<br>

# In[57]:


import json
listNumbers=[1,10,20,30,40,50]
tupleNumbers=(1,5,10,15,20,25)
jsonData1=json.dumps(listNumbers)#python 轉 json
jsonData2=json.dumps(tupleNumbers)
print("串列轉換json的陣列",jsonData1)
print("元組轉換json的陣列",jsonData2)
print("json陣列在Python的資料類型",type(jsonData1))


# 將json格式資料轉成Python資料
# 使用json模組內的loads()

# In[58]:


import json
jsonObj='{"bob":88,"allen":66,"chris":77}'
dictObj=json.loads(jsonObj)
print(dictObj)
print(type(dictObj))


# In[59]:


{"Asia":[{"Japan":"Toyko"},{"Taiwn":"Taipei"}]}  #注意


# In[60]:


import json 
obj='{"Asia":[{"Japan":"Toyko"},{"Taiwan":"Tapei"}]}'
json_obj=json.loads(obj)#json 轉 python
print(json_obj)
print(json_obj["Asia"])
print(json_obj["Asia"][0])
print(json_obj["Asia"][1])
print(json_obj["Asia"][0]["Japan"])


# In[61]:


import json 
dictObj={'bob':88,'allen':66,'chris':77}#字典
fn='py_six/day2-20210724T050933Z-001/day2/save_1.json'
with open(fn,'w') as fnObj:#打開 給 寫入
    json.dump(dictObj,fnObj)#字典 轉 json
with open(fn,'r') as fnObj:#打開 給 讀出
    data=json.load(fnObj)#json 轉 python
print(data)
print(data)


# In[62]:


import json 
objlist=[{"日本":"Japan","首都":"Tykyo"},{'美州':"USA",'首都':'Washington'}]
fn='py_six/day2-20210724T050933Z-001/day2/save_1.json'
with open(fn,'w') as fnObj:
    json.dump(objlist,fnObj)
with open(fn,'r') as fnObj:
    data1=json.load(fnObj)
print(data1)
print(type(data1))


# In[63]:


import json 
objlist=[{"日本":"Japan","首都":"Tykyo"},{'美州':"USA",'首都':'Washington'}]
fn='py_six/day2-20210724T050933Z-001/day2/save_1.json'
with open(fn,'w',encoding='utf-8') as fnObj:#注意  很像
    json.dump(objlist,fnObj,indent=6,ensure_ascii=False)#是  dump 不是dumps
with open(fn,'r',encoding='utf-8') as fnObj:#注意  很像
        kk=json.load(fnObj)#是 load 不是loads
print(kk)


# In[ ]:





# Pandas
# 
# Pandas來自panel、dataframe、series,這三個單
# 字,也是Pandas三個資料結構
# ■ Panel
# ■ DataFrame
# ■ Series

# In[64]:


get_ipython().system('pip install pandas')


# In[ ]:





# Series是一種一維的陣列資料結構
# 陣列可以是整數、浮點數、字串
# 也可以是Python(例如:字串list、字典dict...)
# Numpy的ndarray,純量
# 語法如下:
# pandas.Series(data=None,index=None, dtype=None, options, ...)

# In[65]:


import pandas as pd
s=pd.Series([11,22,33,44,55])
print(s)


# In[66]:


import pandas as pd 
myindex =[3,8,9]
value=[20,55,67]
s=pd.Series(value,index=myindex)
print(s)


# In[67]:


import pandas as pd 
drink=['tea','coca','coffee']
price=[33,12,59]
s=pd.Series(price,index=drink)
print(s)


# DataFrame
# 
# DataFrame是一種二維的陣列資料結構
# 陣列可以是整數、浮點數、字串
# 也可以是Python(例如:字串list、字典dict...)
# Numpy的ndarray,純量
# 語法如下:
# pandas.DataFrame(data=None,index=None, dtype=None, options, ...)
# 
# _______
# 組合一維陣列Series物件成為二維陣列的
# DataFrame
# 
# 55
# pandas.concat([Series1,Series2,... ],axis=1)
# 
# 

# In[68]:


import pandas as pd
years=range(2018,2021)
tokyo=pd.Series([13,15,19],index=years)
hongkong=pd.Series([25,26,27],index=years)
singapore=pd.Series([30,29,31],index=years)
print("\n")
citydf0=pd.concat([tokyo,hongkong,singapore])#預設axis=0
print(type(citydf0))
print(citydf0)
print("\n")
citydf=pd.concat([tokyo,hongkong,singapore],axis=1)
print(type(citydf))
print(citydf)


# In[69]:


import pandas as pd
years=range(2018,2021)
tokyo=pd.Series([13,15,19],index=years)
hongkong=pd.Series([25,26,27],index=years)
singapore=pd.Series([30,29,31],index=years)
citydf=pd.concat([tokyo,hongkong,singapore],axis=1)
cities=['beijing','hongkong','singapore']
citydf.columns=cities#欄位屬性
print(type(citydf))
print(citydf)


# In[70]:


import pandas as pd
data =[{'apple':50,'Orange':28,'Cherry':80},{'apple':50,'Cherry':80}]
fruits = pd.DataFrame(data)
print(fruits)


# In[71]:


import pandas as pd
cities = {'country':['Taiwan', 'Japan', 'Singapore'],'town':['Taipei','Tokyo','Singapore'],'population':[200, 1600, 600]}
citydf = pd.DataFrame(cities)
print(citydf)


# In[72]:


#:前面是橫軸   水果是3種 各一 共三組 放第一筆資料
# _____________城市是 一個字典裡  一個橫軸 有三組  共三筆  ； 第二個橫軸 有三組  共三筆..... 


# In[73]:


import pandas as pd
cities = {'country':['Taiwan', 'Japan', 'Singapore'],'town':['Taipei','Tokyo','Singapore'],'population':[200, 1600, 600]}
rowindex = ['first', 'second', 'third']
citydf = pd.DataFrame(cities, index=rowindex)
print(citydf)


# In[ ]:





# In[74]:


#columns欄名  index列名


# In[75]:


import pandas as pd
cities = {'country':['Taiwan', 'Japan', 'Singapore'],'town':['Taipei','Tokyo','Singapore'],'population':[200, 1600, 600]}
citydf = pd.DataFrame(cities,columns=["town","population"],index=cities["country"])
#citydf.columns=cities (想ˋ一 下\比較 \查資料
print(citydf)


# Series和DataFrame物件完成後,接著可以開始執行資料分析跟處理
# 
# 
# 屬性 說明
# at 使用index和columns內容取得或設定單一元素內容與陣列內容
# iat 用index和columns編號取得或設定單一元素內容
# loc 使用index和columns內容取得或設定整個row或columns資料或陣列內容
# iloc 用index和columns編號取得或設定整個row或columns資料

# Pandas用to_csv()將DataFrame物件寫入CSV檔案
# to_csv(path= None, sep=’,’, header=True,index=True,encoding=None,...)
# path : 檔案路徑
# sep:分隔字元,預設是‘,’
# header:是否保留columns,預設True
# index:是否保留index,預設True
# encoding:檔案編碼方式

# In[76]:


import pandas as pd
course=['Chinese','English','Math','Natural','Society']
chinese=[14,12,10,13,12]
eng=[13,14,11,10,15]
math=[15,8,13,9,15]
nature=[15,10,13,10,15]
social=[12,11,14,9,14]
df=pd.DataFrame([chinese,eng,math,nature,social],columns=course,index=range(1,6))
df.to_csv("py_six/day2-20210724T050933Z-001/day2/university_a.csv")
df.to_csv("py_six/day2-20210724T050933Z-001/day2/university_b.csv",header=False,index=False)


# Pandas用read_csv()將DataFrame物件讀取CSV檔案
# read_csv(path= None, sep=’,’, index_col=None,names=None, encoding=None,userows=None,usecols=None, ...)
# 
# path : 檔案路徑
# sep:分隔字元,預設是‘,’
# header:設定那一row為欄位標籤,預設是0。當參數有names時,此為None。
# 如果所讀取的檔案有欄位標籤時,需設定此header值
# index_col:指出第幾個欄位column是索引,預設是None
# encoding:檔案編碼方式
# nrows:設定讀取前幾個row
# usecols:設定讀取前幾個欄位

# In[77]:


ttr=pd.read_csv("py_six/day2-20210724T050933Z-001/day2/university_b.csv",names=course)
print(ttr)


# 最常使用plot(),基本語法如下:
# plot(x=None, kind = “XX”, title = None, legend=True,rot=None,...)
# 
# kind是選擇繪圖模式,預設是line,常見的選項是bar、hist、box、pie、scatter、...等。
# rot是旋轉刻度

# In[78]:


import pandas as pd 
import matplotlib.pyplot as plt

population=[860,1100,1450,1800,2020,2200,2260]
tw=pd.Series(population,index=range(1950,2011,10))
tw.plot(title='Population in Taiwan')
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()


# In[79]:


import pandas as pd 
import matplotlib.pyplot as plt
cities={'population':[1000,850,800,1500,600,800],'town':['New York','Chicago','Bangkok','Tokyo','Singpore','HongKong']}
tw1=pd.DataFrame(cities,columns=['population'],index=cities['town'])
tw1.plot(title='Population in the world')
plt.xlabel('City')
plt.ylabel('Population')
plt.show( )


# In[80]:


import pandas as pd 
import matplotlib.pyplot as plt
cities={'population':[1000,850,800,1500,600,800],'town':['New York','Chicago','Bangkok','Tokyo','Singpore','HongKong']}
tw2=pd.DataFrame(cities,columns=['population'],index=cities['town'])
tw2.plot(title='Population in the world', kind='bar')#kind參數可更改圖表
plt.xlabel('City')
plt.ylabel('Population')
plt.show( )


# In[ ]:





# pie()常用的語法:
# pie(x,options,...)
# x是一個串列,options表示可以選擇的參數:
# ■ labels:標籤
# ■ colors:顏色
# ■ explode :是否從圓餅圖分離,0表示不分離,數值越大越分離,可
# 從0.1開始
# ■ autopct:表示項目百分比格式,基本語法是“%格式%%”,例如:
# “%1.2f%%”表示整數1位數,小數是2位數

# In[81]:


import  pandas as pd
import matplotlib.pyplot as plt 

fruits=['Apple','Bananas','Grapes','Pear','Oranges']
s=pd.Series([2300,5000,1200,2500,2900],index=fruits,name='Fruits Shop')
explode1=[0.4,0,0,0.2,0]# 圓餅圖 要分離嗎? 數字越大 分越開
s.plot.pie(explode=explode1,autopct='%1.2f%%')# 預設格式:%____%%
plt.show()


# In[ ]:





# In[82]:


get_ipython().system('pip install pandas-datareader#安裝pandas-datareader股票模組')


# In[83]:


import pandas_datareader as pdr
df_2330=pdr.DataReader('2330.TW','yahoo')
print(df_2330)


# In[84]:


import pandas_datareader as pdr
startTime='2020-03-01'
endTime='2020-06-30'
df_2330=pdr.DataReader('2330.TW','yahoo',startTime,endTime)
print(df_2330)


# In[ ]:





# In[ ]:





# Open 開盤價
# High 最高價
# Low 最低價
# Close 收盤價
# Volume 交易量
# Adj Close 經過調整的收盤價

# <font color=#663399 size=40 face=雅黑>day3</font>
# 
# 
# 

# 雖然串列(list),元組(tuple)可以執行一維陣列或
# 多為陣列的運算,但真正在運算時:
# ■ 執行速度慢
# ■ 需要較多的系統資源
# 
# Numpy模組主要是支援多維度空間的陣列與矩陣
# 運算,可以產生矩陣,並擴充到圖表
# import numpy as np

# 陣列(array)類似Python串列(list),不過array資料
# 型態必須是"相同",不同於list可以不同。
# 
# 陣列是程式語言的一種基本資料結構,
# 屬於循序性的資料結構。
# 
# 信箱依序編號,1、2、3、4、5,號碼是存取資料的
# 索引,稱為「一維陣列」。

# 使用linspace()方法,可以產生相同等距的陣列
# ■ linspace(start, end, num) #最常使用簡化的語法
# start是起始值,end是結束值,num產生多少個等距點的的陣列
# 值,預設值是5
# 
# ■ arange(start, stop, step)
# start是起始值如果省略預設值是0,stop是結束值但所產生的陣
# 列不包含此值, step是陣列相鄰元素的間距,預設值是1

# In[85]:


import numpy as np
x1= np.linspace(0,10,num=11)
print(type(x1),x1)# 浮點數ㄛ
x2= np.arange(0,11,1)
print(type(x2),x2)
x3= np.arange(11)
print(type(x3),x3)


# In[ ]:





# In[86]:


import matplotlib.pyplot as plt
import numpy as np

xpt=np.linspace(0,10,500)#建立含500個元素
ypt1=np.sin(xpt)#y陣列的變化
ypt2=np.cos(xpt)
plt.scatter(xpt, ypt1,color=(0,1,0))#綠色
plt.scatter(xpt,ypt2)#預設顏色
plt.show()


# In[87]:


import matplotlib.pyplot as plt
import numpy as np
 
xpt=np.linspace(0,5,500)
ypt=1-0.5*np.abs(xpt-2)
lwidths=(1+xpt)**2
plt.scatter(xpt,ypt,s=lwidths,color=(0,1,0))
plt.show()
rty=plt.scatter(xpt,ypt,s=50,c=ypt,cmap='hsv')
plt.show(rty)


# In[ ]:





# 在scatter()中,增加color的設定參數是c,此時color
# 的值是陣列(或是串列),增加cmap(color map),指
# 定色彩映射值
# https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html

# Numpy模組所建立的陣列資料型態稱
# ndarray(n-dimension array)。ndarray陣列特色如
# 下:
# ■ 陣列大小是固定
# ■ 陣列元素內容的資料型態是相同
# 認識ndarray
# 
# 19
# 
# 屬性 說明
# ndarray.dtype 陣列元素型態
# ndarray.itemsize 陣列元素資料型態大小,單位是位元組
# ndarray.ndim 陣列的維度
# ndarray.shape 陣列維度元素個數的元祖
# ndarray.size 陣列元素個數

# In[88]:


import numpy as np
x=np.array([1,2,3])
print(x.dtype)#列印x陣列元素型態,例如int64,指64位元
print(x.itemsize)#列印x陣列元素大小,一個位元組是8個位元,會回傳8
print(x.ndim)#列印x陣列維度
print(x.shape)#列印陣列外形,3是第1維元素個數
print(x.size)#列印x陣列元素個數


# In[89]:


import numpy as np
x=np.array([1,2,3])
y=x+8
print(y)
print('='*8)
y=np.array([10,20,30])
z=x+y
print(z)
print('='*8)
z=x/y
print(z)
print('='*8)


# In[90]:


import numpy as np
x=np.array([[1,2,3],[4,5,6]])
print(x.dtype)
print(x.itemsize)
print(x.ndim)
print(x.shape)
print(x.size)
print(x)


# x=np.zeros((2,3))

# x=np.ones((2,3))

# In[95]:


import numpy as np
x=np.array([[1,2,3],[4,5,6]])
print(x[0,2])
print(x[1,1])
print("========")
x[1,2]=20
print(x)


# In[104]:


import numpy as np 
x=np.array([[1,2,3],[4,5,6]]) #多維矩陣
print(x[0])#row=0
print(x[0,])#row=0
print(x[0,:])#row=0
print('======')
print(x[:,1])#不管 列  取第一欄
print(list(x))
xx11=np.square(x)
print(xx11)


# In[108]:


u=np.array([[7,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]])
#逗號前面 是 列  ，後面是 欄   ，清清楚楚
print(u[:3,0])
print(u[:2,3:5])
print(u[1:])
print('='*10)
print(u)


# In[109]:


e=np.array([1,2,3,4,5,6])
g=e.reshape(2,3)#想轉幾維  都可以
print(g)
o=g.reshape(3,2)
print(o)


# In[111]:


a=np.array([[1,2,3],[4,5,6]])
y=x.ravel()
print(y)

b=np.array([[2,3,4],[5,6,7]])
z=b.flatten()
print(z)
'''
首先声明两者所要实现的功能是一致的（将多维数组降位一维），两者的区别在于返回拷贝（copy）还是返回视图（view），
numpy.flatten()返回一份拷贝，对拷贝所做的修改不会影响（reflects）原始矩阵，
而numpy.ravel()返回的是视图（view，也颇有几分C/C++引用reference的意味），会影响（reflects）原始矩阵。
————————————————
'''


# In[112]:


import numpy as np 
x=np.array([1,2,3])
y=np.array([5,6,7])
print(np.concatenate([x,y]))
print('='*35)
z=[6,7,8]
print(np.concatenate([x,y,z]))
#使用np.concatanate串接


# In[114]:


import numpy as np
grid=np.array([[1,2,4],[4,7,8]])
print(np.concatenate([grid,grid]))
print('='*90)
print(np.concatenate([grid,grid],axis=1))


# ![00123.png](attachment:00123.png)
# 

# In[119]:


import numpy as np
x=np.array([1,2,6])
grid=np.array([[9,8,7],[6,5,4]])
print(np.vstack([x,grid]))#垂直疊加   放下面
print('='*70)
y=np.array([[33],[33]])
print(np.hstack([grid,y]))#水平疊加   橫橫放後面


# hsplit()將陣列依垂直方向切割
# vsplit()將陣列依水平方向切割
# 1. ...
# 2. y1,y2 = np.hsplit(x,2)
# 3. ...
# 4. y1,y2 = np.vsplit(x,2)

# 向量內積
# 
# 如 A[a1,a2,a3],B[b1,b2,b3]
# A。B=a1*b1+a2*b2+a3*b3
# np.inner(A,B) or  np.dot(A,B)
# 

# In[121]:


import numpy as np 
x=np.array([1,2,5])
y=np.array([4,6,3])
z1=np.inner(x,y)
print(z1)
z2=np.dot(x,y)
print(z2)


# 向量外積
# 
# ![71105.png](attachment:71105.png)

# In[122]:


import  numpy as np
x=np.array([1,2,3])
y=np.array([5,6,7])
z=np.outer(x,y)
print(z)


# <實作>轉置矩陣

# In[123]:


import numpy as np
x=np.arange(10).reshape(5,2)
print(x)
print('='*45)
y1=x.transpose()
print(y1)
print('='*46)
y2=x.T


# In[125]:


import numpy as np 
A=0
X=np.arange(1,101).reshape(10,10)
print(X)
for x in X:
    A+=x
print(type(A))
print('A=',A)
sum=0
for a in A:
    sum+=a
print(type(sum))


# 使用plt.imshow(img, cmap=‘xx’)
# ■ 參數img可以是圖片,也可以是矩陣數據。這個函數常用在機器學
# 習檢測神經網路的輸出

# In[126]:


import numpy as np
import pandas as pd
s=pd.Series(np.arange(0,9,2))
print(s)


# In[127]:


import numpy as np
import pandas as pd
s=pd.Series([1,2,4])
ss=np.square(s)#平方
print(ss)


# In[152]:


import numpy as np
import pandas as pd
df1=pd.DataFrame([[1,2,3],[4,np.nan,6],[7,8,np.nan]])#np.nan  空值
x=df1.isna()
y=df1.notna()
print(df1)
print('='*80)
print(x)
print('='*80)
print(y)
print('='*80+"\n")
print(df1.isnull())
print("\n")
print(df1.isnull().sum())
print('='*80)


# %%

# In[155]:


aa=df1.fillna(0)# nan ;補0
print(aa)
print("\n")
bb=df1.dropna() #刪 nan 的 rows
print(bb)
print("\n")
cc=df1.dropna(axis='columns')# 刪 nan的 columns
print(cc)


# In[156]:


get_ipython().system('pip install scipy')


# 4x+3y = 15
# x-z=1
# 7y+2z=11

# In[158]:


import numpy as np
from scipy import linalg
coeff=np.array([[4,3,0],[1,0,-1],[0,7,2]])
deps=np.array([15,1,11])
ans=linalg.solve(coeff,deps)
print(ans)


# 使用scipy.stats 內的randint()建立指定區間均勻分
# 布的隨機整數,語法如下:
# stats.randint(low, high, size, options) #options其他參數

# In[160]:


import scipy.stats as st
rv=st.randint(low=1,high=11)
xx=rv.rvs(size=5)
print(rv)
print(xx)


# scipy.stats模組,提供統計最常見的函數
# ■ mean(low,high,loc=0):算術平均數 #loc設定mean的算法
# ■ var(low,high,loc=0):變異數
# ■ std(low,high,loc=0):標準差
# ■ median(low,high,loc=0):中位數
# 
# norm()建立常態分佈模型:
# norm(loc=0,scale=1)
# loc是mean預設是0,scale是標準差std預設是1

# In[162]:


import matplotlib.pyplot as plt
import scipy.stats as st
x=st.norm.rvs(size=1200)
plt.hist(x)
plt.ylabel('Times')
plt.show()


# optimization模組
# 
# 內有許多功能,處理最佳化、找最
# 小值、曲線擬合、解方程式的根
# 解一元二次方程式的根
# ■ root(fun, x0, options,...) #options是較少用的參數
# ■ fun是要解的函數名稱,x0是初始迭代值(可以用不同的
# 參數值,會有不同的結果)

# In[188]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

from scipy.optimize import fsolve,root
from scipy.integrate import odeint
def f(lalala):
    x,y=lalala[0],lalala[1]


    return [
        x**2-6*x+8-y,
        2*x+3-y
    ]
solved=fsolve(f,[0,1])
print(solved)

print("Program done!")


'''
plt.plot(f,color='red',label='f1')
plt.plot(f,color='blue',label='f2')
plt.legend()
#plt.title('%.5fx%.5f=y' % (A, B))
plt.show()
'''
print("="*50)

rangex1 = np.linspace(-2,8)
rangey1_1,rangey1_2 = 2*np.sin(rangex1),rangex1-1
plt.figure(1)
plt.plot(rangex1,rangey1_1,'r',rangex1,rangey1_2,'b--')
plt.title('$2sin(x)$ and $x-1$')

def f1(x):
    return np.sin(x)*2-x+1

sol1_root = root(f1,[2])
sol1_fsolve = fsolve(f1,[2])
plt.scatter(sol1_fsolve,2*np.sin(sol1_fsolve),linewidths=9)
plt.show()

## 2、求解線性方程組{3X1+2X2=3;X1-2X2=5}
def f2(x):
    return np.array([3*x[0]+2*x[1]-3,x[0]-2*x[1]-5])

sol2_root = root(f2,[0,0])
sol2_fsolve = fsolve(f2,[0,0])
print(sol2_fsolve) # [2. -1.5]

a = np.array([[3,2],[1,-2]])
b = np.array([3,5])
x = np.linalg.solve(a,b)
print(x) # [2. -1.5]
## 3、求解非線性方程組
def f3(x):
    return np.array([2*x[0]**2+3*x[1]-3*x[2]**3-7,
                    x[0]+4*x[1]**2+8*x[2]-10,
                    x[0]-2*x[1]**3-2*x[2]**2+1])

sol3_root = root(f3,[0,0,0])
sol3_fsolve = fsolve(f3,[0,0,0])
print(sol3_fsolve)

## 4、非線性方程
def f4(x):
    return np.array(np.sin(2*x-np.pi)*np.exp(-x/5)-np.sin(x))
init_guess =np.array([[0],[3],[6],[9]])
sol4_root = root(f4,init_guess)
sol4_fsolve = fsolve(f4,init_guess)
print(sol4_fsolve)
t = np.linspace(-2,12,2000)
y1 = np.sin(2*t-np.pi)*np.exp(-t/5)
y2 = np.sin(t)
plt.figure(2)
a , = plt.plot(t,y1,label='$sin(2x-\pi)e^{-x/5}$')
b , = plt.plot(t,y2,label='$sin(x)$')
plt.scatter(sol4_fsolve,np.sin(sol4_fsolve),linewidths=8)
plt.title('$sin(2x-\pi)e^{-x/5}$ and $sin(x)$')
plt.legend()


# In[194]:


import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def func(x, a, b, c):
    return a * np.exp(-b * x) + c
#定義數據以使其適合某些噪聲：

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, ydata, 'b-', label='data')
#適合函數func的參數a，b，c：

popt, pcov = curve_fit(func, xdata, ydata)
popt
plt.plot(xdata, func(xdata, *popt), 'r-',
label='fit:a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

#將優化限製在以下區域0 <= a <= 3，0 <= b <= 1和0 <= c <= 0.5：

popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
popt

plt.plot(xdata, func(xdata, *popt), 'g--',
label='fit:a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


# In[195]:


get_ipython().system('pip install opencv-python')


# In[ ]:

#%%




import numpy as np
import cv2
img=cv2.imread("D:\桌面/ttt.png")

cv2.imshow('Lena',img)
cv2.waitKey(0)#??????????????????????????????????

# %%

#%%
# In[24]:


import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#讀取圖片 默認為BGR 需要轉成RGB並plt印出來
img = cv.imread("00123.png")
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()


# In[ ]:





# In[ ]:


'''
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#讀取圖片 默認為BGR 需要轉成RGB並plt印出來
img = cv.imread("00123.png")
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)



height, width, channels =img.shape #print height, width,channels
img_updown = np.zeros([height,width, 3], dtype=np.uint8)
for i in range(height):
    for j in range(width):
        img_updown[height-i-1,j] =img[i,j]
cv.imwrite("00123.png",img_updown);

plt.imshow()
plt.show()


# In[ ]:





# In[ ]:


'''

height, width, channels =img.shape #print height,width, channels
img_RL = np.zeros([height,width, 3], dtype=np.uint8)
for i in range(height):
    for j in range(width):
        img_RL[i, width-j-1] =img[i,j]

cv2.imwrite("RL.bmp",img_RL);
'''


# In[ ]:





# In[ ]:


'''
height, width, channels =img.shape #print height,width, channels

img_DIG = np.zeros([height,width, 3], dtype=np.uint8)
for i in range(height):
    for j in range(width):
        img_DIG[j,i]=img[i,j]
cv2.imwrite("DIG.bmp",img_DIG);

'''


# In[ ]:







# In[ ]:





# In[ ]:





# In[ ]:





# #分別代表(影像,頂點座標,對向頂點座標,顏色,線條寬度（-1為填滿）)
# cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# #畫圓型 (影像,圓心座標,半徑,顏色,線條寬度)
# cv.circle(img,(x,y),30,(0,255,0),3)
# #畫多邊形 (設定座標點)
# arr = np.array([[20,20],[30,30],[50,30]],np.int32)
# #多邊形（影像,頂點座標,封閉形,顏色,線條寬度）
# cv.polylines(img, [arr], True, (255, 255, 0), 4)
# #分別代表(影像,頂點座標,對向頂點座標,顏色,線條寬度（-1為填滿）)
# cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# #畫圓型 (影像,圓心座標,半徑,顏色,線條寬度)
# cv.circle(img,(x,y),30,(0,255,0),3)
# #畫多邊形 (設定座標點)
# arr = np.array([[20,20],[30,30],[50,30]],np.int32)
# #多邊形（影像,頂點座標,封閉形,顏色,線條寬度）
# cv.polylines(img, [arr], True, (255, 255, 0), 4)

# In[ ]:




