#%%

#正規表達式
import re  
from bs4 import BeautifulSoup as BS
import os

with open('0001.html','r',encoding='utf8') as fp:
    soup=BS(fp,'html.parser')
print(soup.prettify())


#%%%
regexp=re.compile('男-')
tag_str=soup.find(text=regexp)
print(tag_str)
#%%


regexp1=re.compile('\w+-')  # '+'; 任何字元出現一次 or 很多次
tag_str1=soup.find(text=regexp)
print(tag_str1)


# %%
regexp2=re.compile('\w*-')  # '*' ;任何字元，出現0 次 or 很多次
tag_str2=soup.find(text=regexp2)
print(tag_str2)

# %%
email_reg=re.compile('\w+@\w+\.\w+')
tag_str3=soup.find(text=email_reg)
print(tag_str3)
print("-"*20+'find all' +"-"*20)
tag_list2=soup.find_all(text=email_reg)
print(tag_list2)

# %%
urlreg=re.compile("^http:")
tagurl=soup.find_all(href=urlreg)
print(tagurl)


# %%
#???????????
tagitem=soup.select('#q1 > ul > li:nth-of-type(1) >span')  #nth-child(1)  nth-of-type(1)
print(tagitem[0].string)
#????????????????

# %%
taga=soup.select('p > a' )
print(taga)

print("-"*20)

taga1=soup.select('p a')
print(taga1)

print("-"*20)

taga2=soup.select('a')
print(taga2)

# %%
from bs4 import BeautifulSoup as BS
import requests
url='https://www.ptt.cc/bbs/NBA/index.html'
r=requests.get(url)
r.status_code

soup=BS(r.text,'html.parser')
objtag=soup.select('div.title a')
print('標題的總數是',len(objtag))
print(objtag[3].string)

print("-"*20+'\n'*4+"-"*20)

for i in objtag:
    print(i.string)
# %%
import requests
from bs4 import BeautifulSoup as BS
urlz='http://www.ptt.cc/bbs/Gossiping/index.html'
s=requests.session()
s.post('https://www.ptt.cc/ask/over18',\
    data={'from':'bbs/Gossiping/index.html','yes':'yes'})

res=s.get(urlz)    # 取得 html 介 面
print(res.text,'html.parser')
div_tags=soup.find_all('div',{'class':'title'})   #找到網頁中div 下class=title 的 tag
print(div_tags[0])


print("-"*20+'\n'*4+"-"*20)

for div_tag in div_tags:
    a_tag=div_tag.find('a')  #找到<div  class='title'> 下面的<a>
    if a_tag is not None:
        print(a_tag.text)   #??????
        print(a_tag.string)  #??????????


# %%


# %%

import  requests 
from bs4 import BeautifulSoup as BS
import os

url55='https://www.airbnb.com.tw/s/%E5%8F%B0%E5%8C%97/homes?place_id=ChIJmQrivHKsQjQR4MIK3c41aj8&refinement_paths%5B%5D=%2Fhomes&search_type=section_navigation'
r=requests.get(url55)
soup=BS(r.text,'html.parser')
images=soup.find_all('img')
print(len(images))

print("-"*40)

for image  in  images:
    link=image['src']
    print(link)


# %%
import  requests 
from bs4 import BeautifulSoup as BS
import os

url55='https://www.airbnb.com.tw/s/%E5%8F%B0%E5%8C%97/homes?place_id=ChIJmQrivHKsQjQR4MIK3c41aj8&refinement_paths%5B%5D=%2Fhomes&search_type=section_navigation'
r=requests.get(url55)
soup=BS(r.text,'html.parser')
images=soup.find_all('img')
print(len(images))

j=0
for image in images:
    link=image['src']
    print(link)

    with open('a'+str(j) +'.jpg','wb')as f:
        img=requests.get(link)
        f.write(img.content)
    j+=1





# %%
  


# %%


# %%


# %%


# %%



# %%


# %%


# %%


# %%



