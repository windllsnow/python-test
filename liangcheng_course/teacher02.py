#%%



#%%

import requests
from bs4 import BeautifulSoup
import os

url='https://www.airbnb.com.tw/s/Tainan-City/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=september&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Tainan%20City&place_id=ChIJE_4_lcx8bjQRTnbcpapMf9Q&checkin=2021-08-11&checkout=2021-08-12&source=structured_search_input_header&search_type=autocomplete_click'

r=requests.get(url)

soup=BeautifulSoup(r.text,'html.parser')

images=soup.find_all('img')
i=0
for image in images:
    link=image['src']
    print(link)
   
    with open('a'+str(i)+'.jpg','wb') as f:
        img=requests.get(link)
        f.write(img.content)
    i+=1

#%%

import requests
from bs4 import BeautifulSoup
import os
import re

def imagedownload(url,folder):
    try:
        os.mkdir(os.path.join(os.getcwd(),folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(),folder))
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
        
        
        
url='https://www.airbnb.com.tw/rooms/30408488?check_in=2021-08-27&check_out=2021-08-28&translate_ugc=false&federated_search_id=fb3016d6-9a81-4041-99b3-87c196274f7b&source_impression_id=p3_1628602696_r5ah8CeuNTktx7RV&guests=1&adults=1'
url='https://www.airbnb.com.tw/s/Tainan-City/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=september&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Tainan%20City&place_id=ChIJE_4_lcx8bjQRTnbcpapMf9Q&checkin=2021-08-27&checkout=2021-08-28&source=structured_search_input_header&search_type=autocomplete_click'        
        





# %%















#%%
