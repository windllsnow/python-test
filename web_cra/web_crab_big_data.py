#%%



import requests
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
# 設定cookies的值
cookies = {'over18':'1'}
r = requests.get(url, cookies=cookies)
print(r.text)




#%%
import requests
from bs4 import BeautifulSoup
url = 'http://ehappy.tw/bsdemo1.htm'
html = requests.get(url)
html.encoding = 'UTF-8'
sp = BeautifulSoup(html.text, 'lxml')

print(sp.title)
print(sp.title.text)
print(sp.h1)
print(sp.p)




# %%
from bs4 import BeautifulSoup


import requests
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
# 設定cookies的值
cookies = {'over18':'1'}
r = requests.get(url, cookies=cookies)
print(r.text)





# %%
from bs4 import BeautifulSoup
html = '''
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <p id="p1">我是段落一</p>
      <p id="p2" class='red'>我是段落二</p>
  </body>
</html>
'''
sp = BeautifulSoup(html, 'lxml')
print(sp.select('title'))
print(sp.select('p'))
print(sp.select('#p1'))
print(sp.select('.red'))
# %%
from bs4 import BeautifulSoup
html = '''
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <img src="http://www.ehappy.tw/python.png">
      <a href="http://www.e-happy.com.tw">超連結</a>
  </body>
</html>
'''
sp = BeautifulSoup(html, 'lxml')
print(sp.select('img')[0].get('src'))
print(sp.select('a')[0].get('href'))
print(sp.select('img')[0]['src'])
print(sp.select('a')[0]['href'])
#%%
html = """
<html><head><title>網頁標題</title></head>
<h1>文件標題</h1>
<div class="content">
    <div class="item1">
        <a href="http://example.com/one" class="red" id="link1">First</a>
        <a href="http://example.com/two" class="red" id="link2">Second</a>
    </div>
    <a href="http://example.com/three" class="blue" id="link3">
        <img src="http://example.com/three.jpg">Third
    </a>
</div>
"""

from bs4 import BeautifulSoup
sp = BeautifulSoup(html,'lxml') 

print(sp.title) # <title>網頁標題</title>

print(sp.find('h1')) # <h1>文件標題</h1>

print(sp.find_all('a')) 
print(sp.find_all("a", {"class":"red"}))

data1=sp.find("a", {"href":"http://example.com/one"})
print(data1.text) # First

data2 = sp.select("#link1") 
print(data2[0].text) # First
print(data2[0].get("href")) # http://example.com/one
print(data2[0]["href"])     # http://example.com/one

print(sp.find_all(['title','h1'])) # [<title>網頁標題</title>, <h1>文件標題</h1>]

print(sp.select('div img')[0]['src']) # http://example.com/three.jpg


# %%



import requests
from bs4 import BeautifulSoup
url = 'https://www.taiwanlottery.com.tw/'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
# 找到威力彩的區塊
datas = sp.find('div', class_='contents_box02')
# 開獎期數
title = datas.find('span', 'font_black15').text
print('威力彩期數：', title)
# 開獎號碼
nums = datas.find_all('div', class_='ball_tx ball_green')
# 開出順序
print('開出順序：', end=' ')
for i in range(0,6):
    print(nums[i].text, end=' ')
# 大小順序
print('\n大小順序：', end=' ')
for i in range(6,12):
    print(nums[i].text, end=' ')
# 第二區
num = datas.find('div', class_='ball_red').text
print('\n第二區：', num)












# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
