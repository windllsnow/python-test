#%%
# coding:utf-8
import scrapy
from selenium.webdriver.support import select
class letter789(scrapy.Spider):     #  wiskyscraper  檔名(自己取的)
    name='wisky'
    start_urls=['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']

    def parse(self,response): 
        for products in response.css('div.product-item-info'):          #  div.product-item-info   整個物件欄位   
            try:
                yield{                                                      # 產生資料  字典格式
                    'name':products.css('a.product-item-link::text').get(),  #  a.product-item-link::text  標題
                    'price':products.css('span.price::text').get().replace('£','')  
                     }
            except:
                yield{

                    'name':products.css('a.product-item-link::text').get(),  #  a.product-item-link::text  標題
                    'price':'sold  out'  
                    }
        next_page=response.css('a.action.next').attrib['href'] # a.action next 不能有空格
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
# %%
# 紀錄一下指令  ---在Anaconda prompt)
'''


C:\Users\jason>scrapy startproject  letter789 _______-> 在jason 目錄下 建一個letter789(檔名一定要 英+數)    
C:\Users\jason\letter789> conda install -c conda-forge scrapy    _______->在該目錄下 建構  scrapy 環境


上面程式碼 存C:\Users\jason\letter789\letter789\spiders   重點是  檔案放 spiders 

C:\Users\jason\letter789>    scrapy crawl wisky _______-> class 類別裡  name='wisky' 所以這樣key 


輸出 程式碼  結果'item_scraped_count':100   #這樣就 OK
 

 #Obey robots.txt rules
 ROBOTSTXT_OBEY =False     #違反機器人協定
(解決上述，用IDLE(python的) 開啟 settings.py  改成 True)


C:\Users\jason\letter789>  scrapy crawl wisky

C:\Users\jason\letter789>   scrapy crawl wisky -o  wisky.json   # 存json  可用 記事本開
C:\Users\jason\letter789>  scrapy crawl wisky -o  wisky.csv    # 存csv

# 該程式碼  不能放註解  不懂  幹!!

'''


# %%

print("---------------"*4)

#%%






# %%
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests 
import time


driver= webdriver.Chrome('./chromedriver')
driver.get('http://comic.aya.click/online/best_13672.html?ch=15')

soup=bs(driver.page_source,'lxml')
print('https'+soup.select_one('#TheImg').get('src'))

pp=int(soup.select_one('#pagenum').text.split('/')[1].strip('頁'))
print(pp)



pageurl='https://comic.aya.click/online/best_13672.html?ch=15-{}'
for i in range(pp):
    driver.get(pageurl.format(i+1))
    print('目前在下載第',i+1,'頁')
    soup=bs(driver.page_source,'lxml')
    imgurl='https:'+soup.select_one('#TheImg').get('src')
    res= requests.get(imgurl)
    with open('{}'+format(i)+'.jpg','wb') as f:
        f.write(res.content)
    time.sleep(1)
driver.quit()  # quit 關瀏灠器   close 關 tab
#%%

# 先一個 再多個

from bs4 import BeautifulSoup
import requests
r=requests.get('https://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx')
r.encoding='utf-8'
soup=BeautifulSoup(r.text,'lxml')  #text       page_source

#data1=soup.find_all('h1',class_='font_red18')
#找表格 看開獎歷史記錄是那個表格 class 是什麼

#兩個目標
#class="table_gre td_hm"
#class="table_org td_hm"
# 選第一個表格
data2=soup.find_all('table',class_='table_org td_hm')
print(len(data2))

# 選這個表格中所有數字欄位
# 開始要有空串列
   #要視覺化 必須變成串列 字典
count1=[]
count2=[]

for n in range(0,len(data2)):              #先找出單一表格的所有號碼與數字  
    data3=data2[n].find_all('span')
    for i in range(14,20):
                         #print("第",i,"個欄位")
                         #print(data[1].text)
        print(data3[i].text,"",end="")
                        #for j in range(len(data3)):
                        #print(data3[j].text)
                        #看一下對應的欄位
        count1.append(data3[i].text)
        count2.append(int(data3[i].text))
print(count1)
print(count2)
#count1 是文字型態  count2是整數型態



# 視覺化

alist=[]
for k in range(0,50):
    alist.append(0)
print(alist)
for i in range(1,50):
    print('比對',i)
    
    if i in count2:
        print('目前數字',i,'bingo')
        time=count2.count(i)
        print('time',time)
        alist[i]=time

print(alist)

import matplotlib.pyplot as plt

y=alist

print('alist=',len(y))
x=[]
for i in range(0,50):
    x.append(i+1)
    print(x)
plt.scatter(x,y)
plt.show() 





#%%
import matplotlib.pyplot as plt
x= count2
num_bins=50
n,bins,patches=plt.hist(x,num_bins)
print(n)

print(bins)
plt.show()

#%%
import matplotlib.pyplot as plt

y=alist

print('alist=',len(y))
x=[]
for i in range(0,49):
    x.append(i+1)
    print(x)
plt.scatter(x,y)
plt.show() 


#%%

# %%

# %%

# %%

# %%

#%%

from bs4 import BeautifulSoup
import requests
r=requests.get('https://www.taiwanlottery.com.tw/result_all.htm')
r.encoding='utf-8'
soup=BeautifulSoup(r.text,'html.parser')

data11=soup.find_all('h1',class_='font_red18')
data22=soup.find_all('table',class_='tableWin')

j=['a']

for n in range(0,len(data22)):
    data33=data22[n].find_all('span')
    print(data11[n].text.strip(),end="")
    for i in range(3,len(data33)):
        print(data33[i].text +"",end="") 
        j.append(data33[i].text)
print(j)











#%%

# 下拉式 選單

from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver=webdriver.Chrome()
driver.get('https://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx')
select=Select(driver.find_element_by_name('forma'))  # 注意 s 大寫
select.select_by_index(3)







