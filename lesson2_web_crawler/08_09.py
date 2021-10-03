#%%
#超時設計
from bs4.element import Comment
import requests
try:
    r=requests.get('http://www.googel.com',timeout=0.1)


    print(r.text)
    print("OK______________OK")


except  requests.exceptions.Timeout as ex:

    print("連接失敗:http請求超時AAAAAAAAAAAAa_\n"+str(ex))



#%%

import requests
import os
url='https://www.mirrormedia.com.tw/assets/images/20210721145919-3749d42fb878f45e70be6cffc09b0884-mobile.jpg'
root='D:/test2/'
path=root+url.split('/')[-1]
print(path)

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)              #抓到的內容 r.text, 如果是圖片 r.content
        with open(path, 'wb') as f:      # 文字  w   圖片 wb
            f.write(r.content)
            f.close()
            print('jpg is ok!!!')
    else:
        print("圖片已存在")

except:
    print('抓圖失敗')

# %%

from bs4 import BeautifulSoup  as  BS

h_str='<p>test ,test  !!!!!</p>'


S1=BS(h_str,'lxml')

print(S1)



#%%
import requests
from bs4 import BeautifulSoup as BS

r=requests.get('http://www.google.com')
r.encoding='utf-8'
soup=BS(r.text[1000:1500],'lxml')
print(soup)

# %%
from bs4 import BeautifulSoup as BS
with  open('D:/桌面/0002.html','r',encoding='utf-8') as fp:
    soup=BS(fp,'lxml')
    print(soup.prettify())  #縮排  html 正式格式   漂亮



# %%

import requests
from bs4 import BeautifulSoup as BS

r=requests.get('http://www.pchome.com.tw')
r.encoding='utf-8'
soup=BS(r.text[2000:4000],'lxml')

fp=open('D:/test2/test3.text','w',encoding='utf-8')
fp.write(soup.prettify())
print('已將網頁寫入檔案')
fp.close()


# %%

from bs4 import BeautifulSoup
h_str="<div id='msg' class = 'body  posture' > lesson2 test!!</div>"
soup=BeautifulSoup(h_str,'lxml')
tag=soup.div
print(type(tag))
print('=')
print(tag)  #class 'bs4.element.Tag'

print(tag.name)  #tag主 標籤

print(tag['id'])

print(tag['class'])

print(tag.attrs) #tag 全部
print('===')

print(tag.string) #內容文字#class 'bs4.element.NavigableString'
print(type(tag.string))


print(soup.name)#class 'bs4.BeautifulSoup'
print(type(soup))
print("+++++++++++++++++++++++++")

from bs4 import BeautifulSoup
h_str1="<p><!--註解文字  --></p>"
soup=BeautifulSoup(h_str1,'lxml')
comment=soup.p.string
print(type(comment))#class 'bs4.element.Comment'
print(comment)

#%%

from bs4 import BeautifulSoup as BS

with open('0002.html','r',encoding='utf-8') as fp:
    soup=BS(fp,'lxml')
print(soup.prettify())

#%%
#%%



from bs4 import BeautifulSoup as BS
with open('py_135/0809/0809/Example1.html','r',encoding='utf-8') as fp:
    soup3=BS(fp,'lxml')
taga3=soup3.find('a')
print(taga3)
print(taga3.string)#a->文字


#比 較 哦~~~~~~~~  比較哦~~~~~~~~~


tagp3=soup3.find(name='p')
taga3=tagp3.find(name='a')
print(tagp3.a.string)#p->a->文字
print(taga3.string)#a->文字

#------------------------------------------------------------
print("="*17)

#------------------
tagdiv=soup3.find(id='q2')
taga=tagdiv.find('a')
print(taga.string)

#------------------
print("="*17)
#%%
#------------------
from bs4 import BeautifulSoup as BS
with open('py_135/0809/0809/Example1.html','r',encoding='utf-8') as fp:
    soup3=BS(fp,'lxml')
#     不行    ->   tagli=soup3.find(class='response')
tagli=soup3.find(attrs={'class':'response'})#比較1
tagspan=tagli.find('span')
print(tagspan.string)
#------------------------------------------------------------
print("="*17)

#------------------
tagli=soup3.find(class_='response')#比較2
tagspan=tagli.find('span')
print(tagspan.string)

#%%

from bs4 import BeautifulSoup as BS
with open('py_135/0809/0809/Example1.html','r',encoding='utf-8') as fp:
    soup3=BS(fp,'lxml')
tagp1=soup3.find('p',class_='question')
print(tagp3)
print(type(tagp3))


taglist=soup3.find_all('li',class_='response')
print(taglist)

print("="*17)




tagdiv2=soup3.find('div',class_='question')
print(tagdiv2)
print(tagdiv2.string)


print("="*27)


taglist1=soup3.find_all('p',class_='question',limit=2)# limit 可限制 
print(taglist1)

for aaaa in taglist1:
    print(aaaa.a.string)

print("="*37)


tagdiv3=soup3.find('div',id='q2')
tagall=tagdiv3.find_all(True)
print(tagall)
