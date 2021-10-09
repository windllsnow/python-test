#%%
# coding:utf-8
import scrapy
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
