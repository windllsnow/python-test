from tkinter import*
import os 
from PIL import ImageTK,Image 

def finish_reg():
    name=temp_name.get()
    password=temp_password.get()
    print('目前的目錄',os.getcwd())
    all_ac=os.listdir()


    if name=="" or password=="":
        notif.config(fg='red', text='請填完再走')
        return
    else:
        print('資料已填好')


    for  name_check in all_ac:
        if name== name_check:
            notif.config(fg='red', text=' 這名字用過')
            return
        else:
            newfile = open(name,'w')
            newfile=write(name+'\n')
            newfile=write(password,'\n')
            newfile=close()
            notif.config(fg='green',text='帳號已建立')
            show.config(fg='blue',text=name+'你的帳號已建立')