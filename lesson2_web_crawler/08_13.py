#%%
import requests 
from bs4 import BeautifulSoup
import os

url="https://www.airbnb.com.tw/s/Tainan-City/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=september&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Tainan%20City&place_id=ChIJE_4_lcx8bjQRTnbcpapMf9Q&checkin=2021-08-11&checkout=2021-08-12&source=structured_search_input_header&search_type=autocomplete_click"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')

images=soup.find_all('img')
i=0
for image in images:
    link=image['src']
    print(link)

    with  open('a'+str(i)+'.jpg','wb') as f:
        img=requests.get(link)
        f.write(img.content)
    i+=1



#%%

import requests
from bs4 import BeautifulSoup
import os
import re

url='https://tw.news.yahoo.com/%E5%9C%A8%E7%BE%8E%E5%9C%8B%E6%89%93%E5%88%B0%E7%96%AB%E8%8B%97%E4%BA%86-%E4%BD%95%E5%BA%AD%E6%AD%A1%E6%9B%9D%E6%B3%A8%E5%B0%84%E5%8F%8D%E6%87%89-050504433.html'
imagedownload(url,'c:/test2')  


def imagedownload(url,folder):
    try:
        os.mkdir(os.path.join(os.getcwd(),folder))
        #os.mkdir() 方法用于以数字权限模式创建目录。默认的模式为 0777 (八进制)。
        # 如果目录有多级，则创建最后一级，如果最后一级目录的上级目录有不存在的，则会抛出一个 OSError。
        
        #os.path  获取文件的属性信息。
        #os.path.join()： 將多個路徑組合後返回
        #os.getcwd()返回当前工作目录
        # https://www.runoob.com/python/os-file-methods.html (請看這 有 os 函數 說明)
    except:
        pass
    os.chdir(os.path.join(os.getcwd(),folder))
    #os.chdir() 方法用于改变当前工作目录到指定的路径。
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    images=soup.find_all('img')

    i=0
    for image in images:
        print(images[i])   
        link=image['src']
        print(link)
        
        
        
        if 'jpg' in link or 'jpeg' in link:
            
            with open(str(i)+'.jpg','wb') as f:
                im=requests.get(link)
                f.write(im.content)
                i+=1
        elif 'png' in link:
            with open(str(i)+'.png','wb') as f:
                im=requests.get(link)
                f.write(im.content)
                i+=1
        elif 'gif' in link:
            with open(str(i)+'.gif','wb') as f:
                im=requests.get(link)
                f.write(im.content)
                i+=1                
                
                
        else:
            print('這不是圖片')




#%%
url='https://www.airbnb.com.tw/rooms/30408488?check_in=2021-08-27&check_out=2021-08-28&translate_ugc=false&federated_search_id=fb3016d6-9a81-4041-99b3-87c196274f7b&source_impression_id=p3_1628602696_r5ah8CeuNTktx7RV&guests=1&adults=1'
url='https://www.airbnb.com.tw/s/Tainan-City/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=september&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Tainan%20City&place_id=ChIJE_4_lcx8bjQRTnbcpapMf9Q&checkin=2021-08-27&checkout=2021-08-28&source=structured_search_input_header&search_type=autocomplete_click'     
        

url='https://www.airbnb.com.tw/s/Tainan-City/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=september&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Tainan%20City&place_id=ChIJE_4_lcx8bjQRTnbcpapMf9Q&checkin=2021-08-27&checkout=2021-08-28&source=structured_search_input_header&search_type=autocomplete_click'
url='https://tw.news.yahoo.com/%E5%9C%A8%E7%BE%8E%E5%9C%8B%E6%89%93%E5%88%B0%E7%96%AB%E8%8B%97%E4%BA%86-%E4%BD%95%E5%BA%AD%E6%AD%A1%E6%9B%9D%E6%B3%A8%E5%B0%84%E5%8F%8D%E6%87%89-050504433.html'
imagedownload(url,'c:/test2')   


#%%


from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome('D:/py/chromedriver')
url='http://the-internet.herokuapp.com/login'
driver.get(url)

driver.find_element_by_xpath('.//*[@id="username"]').send_keys('tomsmith')
driver.find_element_by_xpath('.//*[@id="password"]').send_keys('SuperSecretPassword!')
driver.find_element_by_xpath('.//*[@id="login"]/button/i').click()
#  抓定一行

time.sleep(10)
driver.quit()



#browser = webdriver.Firefox() #將geckodriver丟至安裝路徑
#browser.get('http://the-internet.herokuapp.com/login')


#%%
##
##
#
#重要
##
##
from selenium import webdriver 
from bs4 import BeautifulSoup
import time

driver=webdriver.Chrome('D:/py/chromedriver')
driver.maximize_window()
driver.implicitly_wait(10)        #隱藏等待10秒
driver.get('https://hahow.in/courses')    #取得example網頁

print(driver.title)

soup=BeautifulSoup(driver.page_source,'lxml')
fp=open('c:/test2/hahow1.html','w',encoding='utf8')
fp.write(soup.prettify())

print('已存靜態網頁內容…')
fp.close()
time.sleep(5)
driver.quit()





#%%
import time
from selenium import webdriver
driver=webdriver.Chrome('D:/py/chromedriver')
driver.implicitly_wait(10)        #隱藏等待10秒

url='https://hahow.in/courses'
driver.get(url)    #取得動態

items=driver.find_elements_by_css_selector('h4.title') # 模糊可以抓很多



#print(items)
for item in items:
    print(item.text+'\n')
fp.close()
time.sleep(5)
driver.quit()



#TypeError: 'WebElement' object is not iterable
#要處理的物件無法迴圈










#%%
from selenium import webdriver
import time

driver=webdriver.Chrome('D:/py/chromedriver')
driver.maximize_window()
driver.get('https://www.google.com/')
time.sleep(3)
driver.find_element_by_link_text('Gmail').click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.find_element_by_partial_link_text('il').click()




# %%
from selenium import webdriver
import time

driver=webdriver.Chrome('D:/py/chromedriver')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.google.com/')
print(driver.title)
html=driver.page_source
print(html)

time.sleep(5)
driver.quit()

#%%

#測試網站
#自 動化

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome('D:/py/chromedriver')

url='http://the-internet.herokuapp.com/login'
driver.get(url)
time.sleep(1)
driver.find_element_by_xpath('.//*[@id="username"]').send_keys('tomsmith')
time.sleep(1)
driver.find_element_by_xpath('.//*[@id="password"]').send_keys('SuperSecretPassword!')
#username 那" "  ,xpath  那 '' 
time.sleep(1)
driver.find_element_by_xpath('.//*[@id="login"]/button').click()
# 滑鼠右鍵檢查後 ,找到程式碼後,copy  > copy Xpath

time.sleep(5)
driver.quit()


# %%
import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver=webdriver.Chrome('D:/py/chromedriver')
driver.maximize_window()
driver.implicitly_wait(10)        #隱藏等待10秒
driver.get('https://hahow.in/courses')    #取得動態

print(driver.title)

soup=BeautifulSoup(driver.page_source,'lxml')
fp=open('c:/test2/hahow1.html','w',encoding='utf8')
fp.write(soup.prettify())

print('已存靜態網頁內容...')
fp.close()
    
time.sleep(5)
driver.quit()





# %%



# %%



# %%



# %%



# %%



# %%


