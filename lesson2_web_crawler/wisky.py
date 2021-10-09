#%%

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
 # 紀錄一下指令  ---在Anaconda prompt)
'''
上面程式碼 存   C:\Users\jason\wiskyscraper\wiskyscraper\spiders _______->  #\wiskyscraper\spiders  重點是  檔案放 spiders 



# 紀錄一下指令 
 # 紀錄一下指令  ---在Anaconda prompt

上面程式碼 存   C:\Users\jason\wiskyscraper\wiskyscraper\spiders

C:\Users\jason>                  cd wiskyscraper
C:\Users\jason\wiskyscraper>     

C:\Users\jason\wiskyscraper>    scrapy crawl wisky_______-> class 類別裡  name='wisky' 所以這樣key 


 出現 INFO: Spider closed (finished)  完成了










'''
# %%








# %%



# %%



# %%



# %%



# %%



# %%



# %%





# %%
