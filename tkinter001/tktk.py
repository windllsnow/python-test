#%%
'''
from  tkinter import*
win=Tk()
win.title('Login App')

def printinfo():
    print("button test")
    e3=Label(win,text=e1.get()+'會員你好，你的會費沒繳…',font=('Calibri',12))
    e3.grid(row=2,column=1,sticky=E)

Label(win,text='帳號：',font=("Calibri",16).grid(row=0))
Label(win,text='密碼：',font=("Calibri",16).grid(row=1))

e1=Entry(win,width=50)
e1.grid(row=0,column=1,sticky=W)
e1=Entry(win,width=50,show='*')
e1.grid(row=1,column=1,sticky=W)

BOTTOM(win,text='查詢',font=('Calibri',16),command=printinfo).grid(row=2,column=0)

qb=Button(win,test='關閉',command=win.quit)

win.mainloop()

win.destroy()
'''

#%%

from tkinter import *

root=Tk()
root.title("Mywindows")
root.iconbitmap('12.ico')
root.geometry("500x500+500+200")
root.configure(bg='#00ff00')
w=300
h=160

ScreenW=root.winfo_screenwidth()
ScreenH=root.winfo_screenheight()

x1=(ScreenW-w)/2
y1=(ScreenH-h)/2

x11=int(x1)

y11=int(y1)
root.geometry(f"{w}x{h}+{x11}+{y11}")

root.mainloop()

root.destroy()  #不會一直 跑


# %%
from tkinter import*
root=Tk()
root.title("ch2_1")
root.iconbitmap('12.ico')
root.geometry("500x500+500+200")
label=Label(root,text="I like tkinter")
label.pack()          # 包裝與定位元件
print(type(label))
root.mainloop()
root.destroy()


# %%
from tkinter import*
root=Tk()
root.title("ch2_2")
label=Label(root,text="I like again").pack() #  不建議
print(type(label))
root.mainloop()
root.destroy()



# %%

from tkinter import*

root.title("ch2_3")
label=Label(root,text="I like  tkinter",
            fg="blue",bg="yellow",
            height=3,width=15 #字藍 背黃
        )
            
label.pack()
root.mainloop()
root.destroy()

# %%
from tkinter import*
root=Tk()
label=Label(root,text="I kike tkinter",
            fg="#00FF00",bg="#000000",
            height=3,width=15,  
            anchor="nw",
            wraplength=40
            
            )
label.pack()
root.mainloop()
root.destroy()



# %%
from tkinter import*
root=Tk()
label=Label(root,text="I kike tkinter",
            fg="#00FF00",bg="#000000",
            height=3,width=15,  
            anchor="se",
            wraplength=40
            
            )
label.pack()
root.mainloop()
root.destroy()


# %%

from tkinter import*
root=Tk()
label=Label(root,text="I kike tkinter",
            fg="#00FF00",bg="#000000",
            height=3,width=15,  
            anchor=SE,  #  SE     "se"     一樣       wraplength=40
            
            )
label.pack()
root.mainloop()
root.destroy()



# %%
from tkinter import*
root=Tk()
root.title("ch2_7")
label=Label(root,text="I like tkinter",
             fg="blue",bg="yellow",
             height=3,width=14,
             anchor='nw',
             wraplength=40) #文字輸出換行位置
label.pack()
root.mainloop()
root.destroy()


# %%
from tkinter import *
root =Tk()
root.title("ch2_8")
label=Label(root,text="I like tkinter",
                fg="blue",bg="yellow",
                height=10,width=20,
                font="Helvetica 20 bold"
                
                )
label.pack()
root.mainloop()
root.destroy()


# %%

from tkinter import*
root=Tk()
root.title("Ch2_8_1")
label=Label(root,text="I like tkinter",
                fg="blue",bg="yellow",
                height=10,width=20,
                font=("Helvetica", 20 ,"bold")  #元組 字型
                
                )
label.pack()
root.mainloop()
root.destroy()


# %%
from tkinter import*
root=Tk()
root.title("ch2_9")
label=Label(root,text="abcdefghijklmnopqrstuvwxyz",fg="blue",
            bg="lightyellow",wraplength=80,
            justify="center")#最後一行 置中
label.pack()
root.mainloop()
root.destroy()
# %%

from tkinter import*

root=Tk()
root.title("ch2_13")
label=Label(root,bitmap="hourglass")# 位元圖
label.pack()  
root.mainloop()
root.destroy()


# %%
from tkinter import*
root=Tk()
root.title("ch2_14")
label=Label(root,bitmap="gray50",
            compound="left",#圖像在左
            text="我的天空")
label.pack()
root.mainloop()
root.destroy()


# %%

from tkinter import*
root=Tk()
root.title("ch2_7")

label=Label(root,text="raised",relief="raised")#控 widget邊框
label.pack()
root.mainloop()
root.destroy()

# %%
from tkinter import*
root=Tk()
root.title("ch2_18")
label=Label(root,text="raised",relief="raised",
                bg="lightyellow",
                padx=5,pady=10)#標籤文字與標籤區間 左右5  上下10
label.pack()
root.mainloop()
root.destroy()

# %%
from tkinter import *

root = Tk()
root.title("ch2_19")

html_gif = PhotoImage(file="ccc.gif") #  無效 ??，限 gif ok 才對
label=Label(root,image=html_gif)


label.pack()
root.mainloop()
root.destroy()


# %%
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("ch2_19_1")
root.geometry("1400x900")
image=Image.open("yellowstone.jpg") #  無效?? , jpg ok 才對 
lll=ImageTk.PhotoImage(image)
label=Label(root,image=lll)

label.pack()

root.mainloop()
root.destroy()




#%%
from tkinter import *

root = Tk()
root.title("ch2_20")
sseText = """SSE全名是Silicon Stone Education,這家公司在美國,
這是國際專業證照公司,產品多元與豐富."""
sse_gif = PhotoImage(file="sse.gif") #  無效??
label=Label(root,text=sseText,image=sse_gif,bg="lightyellow",
            compound="left")
label.pack()

root.mainloop()





# %%

















# %%



# %%


# %%







# %%



# %%








# %%





from tkinter import *

root = Tk()
app = Frame(root)
hello = Label(root, text="Hello Tk!", width="30", height="5")
hello.pack()
root.mainloop()







# %%


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class Application(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack()

        self.button = ttk.Button(self)
        self.button["text"] = "Click Me!"
        self.button["command"] = self.popup_hello
        self.button.pack()
    
    def popup_hello(self):
        showinfo("Hello", "Hello Tk!")

root = tk.Tk()
app = Application(root)
root.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：tkdemo03.py
# 功能：示範 tkinter 模組
# 作者：張凱慶
# %%

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        self.button = tk.Button(self)
        self.button["text"] = "demo"
        self.button.grid(row=0, column=0, sticky=tk.N+tk.W)
        
        self.checkbutton = tk.Checkbutton(self)
        self.checkbutton["text"] = "demo"
        self.checkbutton.grid(row=1, column=0, sticky=tk.N+tk.W)
        
        self.entry = tk.Entry(self)
        self.entry.grid(row=2, column=0, sticky=tk.N+tk.W)
        
        self.label = tk.Label(self)
        self.label["text"] = "demo"
        self.label.grid(row=3, column=0, sticky=tk.N+tk.W)
                
        self.listbox = tk.Listbox(self)
        self.listbox["height"] = 5
        self.listbox.insert(1, "Python")
        self.listbox.insert(2, "Java")
        self.listbox.insert(3, "Swift")
        self.listbox.insert(4, "JavaScript")
        self.listbox.insert(5, "C")
        self.listbox.grid(row=4, column=0, sticky=tk.N+tk.W)
        
        self.optionList = ("Python", "Java", "Swift")
        self.v = tk.StringVar()
        self.v.set("demo")
        self.optionmenu = tk.OptionMenu(self, self.v, *self.optionList)
        self.optionmenu.grid(row=5, column=0, sticky=tk.N+tk.W)
        
        self.radiobutton = tk.Radiobutton(self)
        self.radiobutton["text"] = "demo"
        self.radiobutton.grid(row=6, column=0, sticky=tk.N+tk.W)
        
        self.scale = tk.Scale(self)
        self.scale.grid(row=7, column=0, sticky=tk.N+tk.W)
        
        self.spinbox = tk.Spinbox(self, from_=0, to=10)
        self.spinbox.grid(row=8, column=0, sticky=tk.N+tk.W)
        
        self.text = tk.Text(self)
        self.text["height"] = 10
        self.text["width"] = 50
        self.text.grid(row=9, column=0, sticky=tk.N+tk.W)
                
root = tk.Tk()
app = Application(root)
root.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：tkdemo03.py
# 功能：示範 tkinter 模組
# 作者：張凱慶




#%%
