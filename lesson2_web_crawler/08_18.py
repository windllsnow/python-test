#%%
import pandas as pd
from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

browser= webdriver.Chrome('./chromedriver')
browser.implicitly_wait(10)
url='http://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1'
browser.get(url)
time.sleep(5)
area=browser.find_element_by_id('onetrust-accept-btn-handler') # 擋的box出現 ，的解決方法~/關閉區域選單
area.click()   

pages_remaining=True
page_num=1


while pages_remaining:
#用BeasutifulSoup 剖析 html網頁
    soup=BeautifulSoup(browser.page_source,'lxml')
    table=soup.select_one('body > main > div > div > div.row > div > div > nba-stat-table > div.nba-stat-table > div.nba-stat-table__overflow')# class 都省略

    df=pd.read_html(str(table)) # 注意str()  不然 不會 列出 NAN

#print(df[0].to_csv())

    df[0].to_csv("All_players_stats"+str(page_num)+'.csv')
    print("儲存頁面： ",page_num)

    

    try:
# 自動按下 一 頁
        next_link=browser.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[3]/div/div/a[2]")
        next_link.click()                # 游 標 按下 [下一頁的icon]
        print('已切換至第',page_num,'頁') # page_num此時=1 ，但頁面已到2//最後網頁到第六頁 程式就跳出迴圈了
        time.sleep(5)
        if page_num<5:
            page_num+=1
        else:
            pages_remaining=False
    except Exception:
        pages_remaining=False
        print('此頁沒有內容')

browser.quit()



# %%
# _________多加一個  " 抓 幾頁"__________
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

srt=int(input("你想抓幾頁? "))



browser= webdriver.Chrome('./chromedriver')
browser.implicitly_wait(10)
url='http://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1'
browser.get(url)
time.sleep(5)
area=browser.find_element_by_id('onetrust-accept-btn-handler') # 擋的box出現 ，的解決方法~/關閉區域選單
area.click()   

pages_remaining=True
page_num=1

while pages_remaining:
#用BeasutifulSoup 剖析 html網頁
    soup=BeautifulSoup(browser.page_source,'lxml')
    table=soup.select_one('body > main > div > div > div.row > div > div > nba-stat-table > div.nba-stat-table > div.nba-stat-table__overflow')# class 都省略

    df=pd.read_html(str(table)) # 注意str()  不然 不會 列出 NAN

#print(df[0].to_csv())

    df[0].to_csv("All_players_stats"+str(page_num)+'.csv')
    print("儲存頁面： ",page_num)

    

    try:
# 自動按下 一 頁
        next_link=browser.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[3]/div/div/a[2]")
        next_link.click()                #
        print('已切換至第',page_num,'頁') # 
        time.sleep(5)
        if page_num <srt and (page_num in range(1,6)): 
            page_num+=1
        else:
            pages_remaining=False
    except Exception:
        pages_remaining=False
        print('此頁沒有內容')

browser.quit()





# %%
# bs4 單頁，簡單 網站內容

# selenium 自動化測試，中型網站，動態網頁

# scrapy 大型網站，架構來爬取


#%%
# conda install -c conda-forge scrapy

#y

# -c找頻道  , 頻道名稱 conda-forge
# 
# 
# 
# 在 Anaconda Prompt 輸入  scrapy shell

#fetch()  是 下載網頁模式
#fetch("http://www.yahoo.com.tw") , crawled(200)  請求成功
#print(response.text)  列出網頁的html 的文字內容
 
# %%
'''
語法：先fetch 網址，view(response)看內容
response.css( 'css選擇器內容 : : text’).extract ( )   
_________________________________________extract=萃取全部, 等同 getall( )
extract_first=一個, 等同 get( )

___________________________  請注意文字要加 ‘ ‘

extract( ) 是舊版， get( )是新版
以之前的pttnba為例

請注意要偵測的css或是tag要全部紅色
url=‘http://www.ptt.cc/bbs/NBA/index.html’
fetch(url)


response.css(‘#topbar a.board : : text’).extract( )     請注意文字要加 ‘ ‘
response.css('div.r-ent > div.title > a::text').extract()


請注意 xpath內的文字要全變色才算有讀取


1 打開Anaconda Prompt
2 cd 進入 Anaconda3\envs\scrapyws  # 沒有的話 建一個scrapyws
3 conda install protego



spiders的目錄：py爬蟲程式在此目錄
items  定義要擷取的欄位
settings 設定專案延遲時間與輸出
	    內有ROBOTSTXT_OBEY=False (爬蟲協定) 
                的設定
pipeline 客製化處理資料，可以自行
	       寫程式碼
spiders 主要爬蟲程式的儲存位置
	


去看 ptt     難爆!!!!!!!!


'''

# %%
# coding:utf-8
import scrapy
class wiskyscraper(scrapy.Spider):     #  wiskyscraper  檔名(自己取的)
    name='wisky'
    start_urls=['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']

    def parse(self,response):
        for products in response.css('div.product-item-info'):          #  div.product-item-info   整個物件欄位   
            yield{                                                      # 產生資料  字典格式
                'name':products.css('a.product-item-link::text').get()  #  a.product-item-link::text  標題





            }




# %%

# 紀錄一下指令 
 # 紀錄一下指令  ---在Anaconda prompt
'''
上面程式碼 存   C:\Users\jason\wiskyscraper\wiskyscraper\spiders

C:\Users\jason>                  cd wiskyscraper
C:\Users\jason\wiskyscraper>     

C:\Users\jason\wiskyscraper>    scrapy crawl wisky

 出現 INFO: Spider closed (finished)  完成了
'''
# %%


