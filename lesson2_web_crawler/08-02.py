#%%
from tkinter import *
import os
from PIL import ImageTk,Image 

#函數

def finish_reg():
    name=temp_name.get()          #填入的名字設為name
    password=temp_password.get()   #填人的密碼為password
    print('目前的目錄是',os.getcwd())
    all_ac=os.listdir()      #可以查到目錄中所有物件
    
    
    if name=="" or password=="":
        notif.config(fg='red',text='請填完資料再確定')
        return
    else:
        print("資料已填好")

      #__________________注意下面__________________
    for name_check in all_ac:          #對於目錄中的所有檔案
        if name==name_check:
            notif.config(fg='red',text='這個名字已經有人使用')
            return
        else:
           newfile=open(name,'w')
           newfile.write(name+'\n')              
           newfile.write(password+'\n')              
           newfile.close()
           notif.config(fg='green',text='帳號已建立')              
           show.config(fg='blue',text=name+'您的帳號已建立')       
        #_____________注意上面_____________________________________
def register():
    global temp_name
    global temp_password
    global notif
    global show
    #print('註冊測試')
    reg_sc=Toplevel(master)
    reg_sc.title('註冊用視窗')
    #reg_sc.iconbitmap('12.ico')
    
    #輸入資料格式
    temp_name=StringVar()
    temp_password=StringVar()
    
    #label
    Label(reg_sc,text='請輸入您的資料，再進行註冊',font=('Calibli',12)).grid(row=0,sticky=N,pady=10)
    Label(reg_sc,text='姓名',font=('Calibli',12)).grid(row=1,sticky=W)
    Label(reg_sc,text='密碼',font=('Calibli',12)).grid(row=2,sticky=W)
    
    #錯誤資訊回傳
    notif=Label(reg_sc,text="")
    notif.grid(row=5,sticky=W)
    show=Label(reg_sc,text="")
    show.grid(row=5,sticky=E)
    
    
    #entry
    Entry(reg_sc,textvariable=temp_name).grid(row=1,column=0)
    Entry(reg_sc,textvariable=temp_password,show='*').grid(row=2,column=0)
    
    #button
    Button(reg_sc,text='確認註冊',font=('Calibli',12),command=finish_reg).grid(row=3,sticky=N, pady=10)
    
    
    
    
    
def login():
    print('登入測試')

#主畫面
master=Tk()
master.title('Banking APP')
master.iconbitmap('12.ico')
#放圖片
img=Image.open('secure1.jpg')
img=img.resize((150,150))
img=ImageTk.PhotoImage(img)

#標籤
Label(master,text='Security Bank System',font=('Calibri',14)).grid(row=0,sticky=N,pady=10)
Label(master,text='你最值得信賴的銀行',font=('Calibri',12)).grid(row=1,sticky=N)
Label(master,image=img).grid(row=2,sticky=N,pady=15)

#按鈕
Button(master,text='Register',font=('Calibri',12),width=20,command=register).grid(row=3,sticky=N)
Button(master,text='Login',font=('Calibri',12),width=20,command=login).grid(row=4,sticky=N)


master.mainloop()
#label





















#%%


#%%
import scrapy
import bs4
 
 


class InsideSpider(scrapy.Spider):
    name = 'inside'
    allowed_domains = ['www.inside.com.tw']
    start_urls = ['https://www.inside.com.tw/tag/ai']
 
    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        titles = soup.find_all('h3', {'class': 'post_title'})
        for title in titles:
            print(title.text.strip())
