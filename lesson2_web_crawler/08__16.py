#%%



from selenium import webdriver
import pandas as pd
url='https://www.youtube.com/user/jason11160/videos'

driver=webdriver.Chrome()
driver.get(url)

#找同類型的多數物件 class單一, xpath 較 ok

videos=driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')# 注意 是elements

video_list=[]
for video in videos:
    title=video.find_element_by_xpath('//*[@id="video-title"]').text
    views=video.find_element_by_xpath('//*[@id="metadata-line"]/span[1]').text
    when=video.find_element_by_xpath('//*[@id="metadata-line"]/span[2]').text

    vid_item={

      'title':title,
      'views':views,
      'posted':when

    }

    video_list.append(vid_item)
df=pd.DataFrame(video_list)
df2=df.sort_values('views',ascending=True)
df2

#%%

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup, element
import time

browser=webdriver.Chrome('./chromedriver')

browser.get('http://rent.591.com.tw')
time.sleep(10)

myarea=browser.find_element_by_xpath('//*[@id="rent-list-app"]/div/section[1]/div[1]')
myarea.click()

time.sleep(10)

myarea1=browser.find_element_by_xpath('//*[@id="rent-list-app"]/section/div/div/p/a[6]')
myarea1.click()

time.sleep(10)


# area=browser.find_element_by_id('area-box-close') # 擋的box出現 ，的解決方法~/關閉區域選單
# area.click()   


#設定要翻頁的頁數 並 下載

for page in range(1,6):
	soup =BeautifulSoup(browser.page_source,'html.parser')
	elements=soup.find_all('div',{'class':'rent-item-right'})
	#print(elements)
	print('='*20, '第',page,'頁總共有',len(elements),'筆資料','='*10)
	for element in elements:
		title=element.find('div',{'class':'item-title'}).getText().strip()
		print(title+'\n')
# 由 class name 來翻頁
page_next=browser.find_element_by_class_name('pageNext')
page_next.click()
time.sleep(5)
   

# %%
'''
<section class="vue-list-rent-item"><a href="https://rent.591.com.tw/rent-detail-11497437.html" target="_blank"><div class="rent-item-left"><div class="vue-public-carousel-wrap"><div class="vue-public-carousel"><ol class="indicators"><li class="active"></li><li class=""></li></ol> <ul class="carousel-list" style="left: 0px; width: 510px;"><li><img data-original="https://img2.591.com.tw/house/2021/09/29/163290293939675267.jpg!510x400.jpg" src="https://img2.591.com.tw/house/2021/09/29/163290293939675267.jpg!510x400.jpg" alt="南紡夢時代商圈" class="obsever-lazyimg"></li><li><img data-original="https://img2.591.com.tw/house/2021/09/29/163290293939746427.jpg!510x400.jpg" src="https://img2.591.com.tw/house/2021/09/29/163290293939746427.jpg!510x400.jpg" alt="南紡夢時代商圈" class="obsever-lazyimg"></li></ul> <div class="public-carousel-left"><i class="fa fa-angle-left"></i></div> <div class="public-carousel-right"><i class="fa fa-angle-right"></i></div></div> <ul class="carousel-list-tags"><li class="gold">
            黃金曝光
        </li> <!----></ul> <!----></div></div> <div class="rent-item-right"><div class="item-title">
                    南紡夢時代商圈
                

'''



# %%

'''
<div class="item-title">
                    近台南通轉運站、二中、成大並附第四台網路
                    <!----></div>
(((((((((((((copy outerHtml)))))))))))))
			(((((((copy element)))))))		
					
#rent-list-app > div > div.list-container-content > div >
#  section.vue-list-rent-content > div > section:nth-child(1) > a >
#  div.rent-item-right > div.item-title
((((((((((((((按copy selector會有路徑))))))))))))))
'''
# %%
import pandas as pd
from selenium import webdriver
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

soup=BeautifulSoup(browser.page_source,'lxml')
table=soup.select_one('body > main > div > div > div.row > div > div > nba-stat-table > div.nba-stat-table > div.nba-stat-table__overflow')# class 都省略

df=pd.read_html(str(table)) # 注意str()  不然 不會 列出 NAN
df


# %%


# %%


# %%



# %%



# %%



# %%
