#%%
# ch7_16.py
from selenium import webdriver
import time

url = 'https://www.google.com'
email = input('請輸入你的Google Email的帳號 : ')
pwd = input('請輸入你的Google Email的密碼 : ')

driverPath = 'D:\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
browser.get(url)                    # 網頁下載至瀏覽器
time.sleep(3)
browser.find_element_by_xpath('//*[@id="gb"]/div/div[2]/a').click()                 # 按登入鈕
browser.find_element_by_id('identifierId').send_keys(email) # 輸入帳號
time.sleep(3)

# 按繼續鈕
browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
time.sleep(3)

# 輸入密碼
browser.find_element_by_xpath("//input[@type='password']").send_keys(pwd)
time.sleep(3)

# 按繼續鈕
browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
time.sleep(3)


#%%
# ch7_17.py
from selenium import webdriver
import time

url = 'https://opendata.epa.gov.tw/data/contents/aqi/'

driverPath = 'D:\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
browser.get(url)                    # 網頁下載至瀏覽器
time.sleep(20)
browser.find_element_by_link_text('JSON').click()      # 按JSON鈕
time.sleep(3)

browser.find_element_by_link_text('XML').click()        # 按XML鈕
time.sleep(3)

browser.find_element_by_link_text('CSV').click()        # 按CSV鈕
time.sleep(3)



#%%