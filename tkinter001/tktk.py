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
from tkinter import font

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


from tkinter import*
counter=0                                # 計數的全域變數
def run_counter(digit):                 # 數字變數內容的更動
    def counting():                     # 更動數字方法
        global counter                  # 定義這是全域變數
        counter+=1
        digit.config(text=str(counter))  #列出標籤數字內容
        digit.after(1000,counting)      # 隔一秒後呼叫counting
    counting()                          # 啟動呼叫
root=Tk()
root.title("ch2_23")
digit=Label(root,bg="yellow",fg="blue",
            height=3,width=10,
            font="helvetic 20 bold")
digit.pack()
run_counter(digit)            # 呼叫數字更動方法
root.mainloop()
root.destroy()







# %%

from tkinter import *

root = Tk()
root.title("ch2_24")

label=Label(root,text="raised",relief="raised",
            bg="lightyellow",
            padx=5,pady=10,
            cursor="heart")     # 滑鼠外形
label.pack()

root.mainloop()
root.destroy()


# %%
from tkinter import *

root = Tk()
root.title("ch2_25")
label=Label(root,text="I like tkinter")
label.pack()        # 包裝與定位元件
print(label.keys())# 回傳全部 所有label方法的參數(optiob)

root.mainloop()
root.destroy()

# %%

from tkinter import *
from tkinter.ttk import Separator

root = Tk()
root.title("ch2_26")

myTitle = "一個人的極境旅行"
myContent = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""

lab1 = Label(root,text=myTitle,
             font="Helvetic 20 bold")
lab1.pack(padx=10,pady=10)

sep = Separator(root,orient=HORIZONTAL)    #HORIZONTAL水平分隔線　　　VERTICAL　垂直分隔線｀
sep.pack(fill=X,padx=5)

lab2 = Label(root,text=myContent)
lab2.pack(padx=10,pady=10)

root.mainloop()





# %%

from tkinter import*
window=Tk()
window.title("CH3_1")
lab1=Label(window,text="明志科技大學",
            bg="lightyellow")
lab2=Label(window,text="長庚大學",
            bg="lightgreen")
lab3=Label(window,text="長庚科技大學",
            bg="lightblue")
lab1.pack()
lab2.pack()
lab3.pack()
window.mainloop()
window.destroy()

# %%

from tkinter import*
window=Tk()
window.title("ch3_2")               # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)   
lab1.pack(side=BOTTOM)  # TOP BOTTOM LEFT RIGHT
lab2.pack(side=RIGHT)
lab3.pack(side=LEFT) 
window.mainloop()
window.destroy()



# %%
from tkinter import*
Reliefs=["flat","groove","raised","ridge","solid","sunken"]
root=Tk()
root.title("ch3_5")
for Relief in Reliefs:
    Label(root,text=Relief,relief=Relief,
            fg="blue",
            font="Times 20 bold").pack(side=LEFT,padx=10)
root.mainloop()
root.destroy()
# %%
from tkinter import *

bitMaps = ["error","hourglass","info","questhead","question",
           "warning","gray12","gray25","gray50","gray75"]

root = Tk()
root.title("ch3_5_1")

for bitMap in bitMaps:
    Label(root,bitmap=bitMap).pack(side=LEFT,padx=5)

root.mainloop()
root.destroy()


# %%

from tkinter import *

window = Tk()
window.title("ch3_6")               # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack(fill=X)       # 填滿X軸包裝與定位元件       
lab2.pack(pady=10)      # y軸增加10像素
lab3.pack(fill=X)       # 填滿X軸包裝與定位元件
window.mainloop()
window.destroy()
# %%
from tkinter import *

window = Tk()
window.title("ch3_7")               # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack(fill=X,pady=10)           # 填滿X軸,Y軸增加10像素
lab2.pack(pady=10)                  # Y軸增加10像素
lab3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()
window.destroy()


# %%
from tkinter import *

window = Tk()
window.title("ch3_10")               # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack(ipady=22)                     
lab2.pack(ipadx=4)          # ipadx=4包裝與定位元件
lab3.pack(ipady=34)


window.mainloop()
window.destroy()

# %%


from tkinter import *

root = Tk()
root.title("ch3_12")
root.geometry("300x180")            # 設定視窗勘寬300高180
oklabel=Label(root,text="OK",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="blue") # 藍底白字
oklabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             padx=10,pady=10)       # x和y軸間距皆是10

root.mainloop()






# %%
from tkinter import *

root = Tk()
root.title("ch3_13")
root.geometry("300x180")            # 設定視窗勘寬300高180
oklabel=Label(root,text="OK",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="blue") # 藍底白字
oklabel.pack(anchor=S,side=LEFT,   # 從右開始在南方配置
             padx=10,pady=10)       # x和y軸間距皆是10
nolabel=Label(root,text="NO",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="red")  # 藍底白字
nolabel.pack(anchor=N,side=RIGHT,   # 從右開始在北方配置
             padx=10,pady=10)        # y軸間距皆是10


root.mainloop()




# %%

from tkinter import *

window = Tk()
window.title("ch3_15")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack(side=LEFT,fill=Y)                   # 填滿X軸包裝與定位元件
lab2.pack(fill=X)                   # 填滿Y軸包裝與定位元件
lab3.pack(fill=BOTH,expand=True)                   # 填滿X軸包裝與定位元件

window.mainloop()



# %%

from tkinter import *

root = Tk()
root.title("ch3_23")
root.geometry("300x180")   

print("執行前",root.pack_slaves())
oklabel=Label(root,text="OK",
            font="Times 20 bold",
            fg="white",bg="blue")
oklabel.pack(anchor=S,side=RIGHT,
            padx=10,pady=15)
nolabel=Label(root,text="no",
                font="Times 20 bold",
                fg="white",bg="red")
nolabel.pack(anchor=S,side=RIGHT,
                pady=10)
print("執行後",root.pack_slaves())
root.mainloop()


# %%

from tkinter import *

window = Tk()
window.title("ch3_25")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
             bg="lightyellow",      # 標籤背景是淺黃色
             width=15)              # 標籤寬度是15     
lab2 = Label(window,text="長庚大學",
             bg="lightgreen",       # 標籤背景是淺綠色
             width=15)              # 標籤寬度是15            
lab3 = Label(window,text="長庚科技大學",
             bg="lightblue",        # 標籤背景是淺藍色
             width=15)              # 標籤寬度是15
lab1.grid(row=0,column=0)
lab2.grid(row=1,column=2)
lab3.grid(row=2,column=1)
window.mainloop()
# %%

from tkinter import *

window = Tk()
window.title("ch3_26")              # 視窗標題
lab1 = Label(window,text="標籤1",relief="raised")
lab2 = Label(window,text="標籤2",relief="raised")
lab3 = Label(window,text="標籤3",relief="raised")
lab4 = Label(window,text="標籤4",relief="raised")
lab5 = Label(window,text="標籤5",relief="raised")
lab6 = Label(window,text="標籤6",relief="raised")
lab7 = Label(window,text="標籤7",relief="raised")
lab8 = Label(window,text="標籤8",relief="raised")
lab1.grid(row=0,column=0,rowspan=2,columnspan=2)
lab2.grid(row=0,column=1)
lab4.grid(row=0,column=3,rowspan=2)
lab5.grid(row=1,column=0)


lab7.grid(row=1,column=2)





window.mainloop()


# %%
from tkinter import *

window = Tk()
window.title("ch3_30")              # 視窗標題
lab1 = Label(window,text="標籤1",relief="raised")
lab2 = Label(window,text="標籤2",relief="raised")
lab3 = Label(window,text="標籤3",relief="raised")
lab4 = Label(window,text="標籤4",relief="raised")
lab5 = Label(window,text="標籤5",relief="raised")
lab6 = Label(window,text="標籤6",relief="raised")
lab7 = Label(window,text="標籤7",relief="raised")
lab8 = Label(window,text="標籤8",relief="raised")
lab1.grid(row=0,column=0,padx=5,pady=5)
lab2.grid(row=0,column=1,padx=5,pady=5)
lab3.grid(row=0,column=2,padx=5,pady=5)
lab4.grid(row=0,column=3,padx=5,pady=5)
lab5.grid(row=1,column=0,padx=5)
lab6.grid(row=1,column=1,padx=5)
lab7.grid(row=1,column=2,padx=5)
lab8.grid(row=1,column=3,padx=5)

window.mainloop()



# %%
from tkinter import *

window = Tk()
window.title("ch3_32")              # 視窗標題
lab1 = Label(window,text="明志工專")
lab2 = Label(window,bg="yellow",width=20)
lab3 = Label(window,text="明志科121263563大")
lab4 = Label(window,bg="aqua",width=10)
lab5 = Label(window,bg="blue",width=5)
lab6 = Label(window,bg="red",width=5)
lab7 = Label(window,bg="pink",width=5)
lab1.grid(row=0,column=0,padx=5,pady=5,sticky=W)  # 左
lab2.grid(row=0,column=1,padx=5,pady=5)
lab3.grid(row=1,column=0,padx=5)
lab4.grid(row=1,column=1,padx=5,sticky=E)  # 右
lab5.grid(row=2,column=0,padx=5,sticky=E+S)  # 拉長
lab6.grid(row=2,column=1,padx=5,sticky=N+S)  # 拉長
lab7.grid(row=3,padx=5,sticky=N+S+W+E)       # 拉長
window.mainloop()


# %%

from tkinter import*
root=Tk()
root.title("ch3_35")
Color=["red","orange","yellow","green","blue","purple"]
r=0
for color in Color:
    Label(root,text=color,relief="groove",width=20).grid(row=r,column=0)
    Label(root,bg=color,relief="ridge",width=20).grid(row=r,column=1)
    r+=1
root.mainloop()
# %%


from tkinter import *

root = Tk()
root.title("ch3_35_1")

root.rowconfigure(1, weight=1)      #????
root.columnconfigure(0, weight=1)   #????

lab1 = Label(root,text="Label 1",bg="pink")
lab1.grid(row=0,column=0,padx=5,pady=5)

lab2 = Label(root,text="Label 2",bg="lightblue")
lab2.grid(row=0,column=1,padx=5,pady=5)

lab3 = Label(root,bg="yellow")
lab3.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

root.mainloop()

# %%

from tkinter import *

root = Tk()
root.title("ch3_35_2")

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

lab1 = Label(root,text="Label 1",bg="pink")
lab1.grid(row=0,column=0,padx=5,pady=5,stick=W)

lab2 = Label(root,text="Label 2",bg="lightblue")
lab2.grid(row=0,column=1,padx=5,pady=5)

lab3 = Label(root,bg="yellow")
lab3.grid(row=1,column=0,columnspan=2,padx=5,pady=5,
          sticky=N+S+W+E)

root.mainloop()

#%%


# %%
from tkinter  import*
root=Tk()
root.title("ch3_39")
root.geometry("640x480")

night=PhotoImage(file="night.png") #  有問題
label=Label(root,image=night)
label.place(relx=0.1,rely=0.1,relheight=0.8)

root.mainloop()
root.destroy()



# %%
from tkinter import *

root = Tk()
root.title("ch3_38")
root.geometry("640x480")

night = PhotoImage(file="night.png")
label=Label(root,image=night)
label.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

root.mainloop()

#%%
# ch3_36.py
from tkinter import *

window = Tk()
window.title("ch3_36")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.place(x=0,y=0)                 # 直接定位
lab2.place(x=30,y=50)               # 直接定位
lab3.place(x=60,y=100)              # 直接定位

window.mainloop()

# %%

from tkinter import *

root = Tk()
root.title("ch3_37")
root.geometry("640x480")

night = PhotoImage(file="night.png")     #  有問題
lab1 = Label(root,image=night)
lab1.place(x=20,y=30,width=200,height=120)
snow = PhotoImage(file="snow.png")      # 影像snow
lab2 = Label(root,image=snow)
lab2.place(x=200,y=200,width=400,height=240)

root.mainloop()

# %%
from tkinter import*

def msgShow():
    label["text"]="I love Python"
    label["bg"]="lightyellow"
    label["fg"]="blue"

root=Tk()
root.title("ch4_1")
label=Label(root)
btn=Button(root,text="列印訊息",command=msgShow)
label.pack()
btn.pack()

root.mainloop()

# %%
from tkinter import*
def msfShow():
    label.config(text="I love Python",bg="lightyellow",fg="blue")  # 建立or更改 屬性
root=Tk()
root.title("ch4_2")
label=Label(root)
btn=Button(root,text="列印訊息",command=msfShow)
label.pack()
btn.pack()
root.mainloop()
root.destroy()
#%%

from tkinter import *

def msgShow():
    label.config(text="I love Python",bg="lightyellow",fg="blue")
      
root = Tk()
root.title("ch4_3")                 # 視窗標題
label = Label(root)                 # 標籤內容             
btn1 = Button(root,text="列印訊息",width=15,command=msgShow)
btn2 = Button(root,text="結束",width=15,command=root.destroy) # 關視窗
label.pack()                      
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)

root.mainloop()






# %%
from tkinter import *

counter = 0                                 # 計數的全域變數
def run_counter(digit):                     # 數字變數內容的更動
    def counting():                         # 更動數字方法
        global counter                       #定義這是全域變數
        counter += 1                        
        digit.config(text=str(counter))     # 列出標籤數字內容
        digit.after(1000,counting)          # 隔一秒後呼叫counting
    counting()                              # 持續呼叫

root = Tk()
root.title("ch4_4")
digit=Label(root,bg="yellow",fg="blue",     
            height=3,width=10,              
            font="Helvetica 20 bold")       
digit.pack()
run_counter(digit)                          # 呼叫數字更動方法
Button(root,text="結束",width=15,command=root.destroy).pack(pady=10)

root.mainloop()

# %%
from tkinter import *

def yellow():                   # 設定視窗背景是黃色
    root.config(bg="yellow")
def blue():                     # 設定視窗背景是藍色
    root.config(bg="blue")
    
root = Tk()
root.title("ch4_5")
root.geometry("300x200")        # 固定視窗大小
# 依次建立3個鈕
exitbtn = Button(root,text="Exit",command=root.destroy) 
bluebtn = Button(root,text="Blue",command=blue)
yellowbtn = Button(root,text="Yellow",command=yellow)
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5) # 靠下靠右  最先
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

root.mainloop()



# %%
from tkinter import *

def bColor(bgColor):          # 設定視窗背景顏色
    root.config(bg=bgColor)
    
root = Tk()
root.title("ch4_5")
root.geometry("300x200")        # 固定視窗大小
# 依次建立3個鈕
exitbtn = Button(root,text="Exit",command=root.destroy)
bluebtn = Button(root,text="Blue",command=lambda:bColor("blue"))
yellowbtn = Button(root,text="Yellow",command=lambda:bColor("yellow"))
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

root.mainloop()


# %%







# %%

#%%
from tkinter import *

def msgShow():
    label.config(text="I love Python",bg="lightyellow",fg="blue")
      
root = Tk()
root.title("ch4_6")                                 # 視窗標題
label = Label(root)                                 # 標籤內容

sunGif = PhotoImage(file="sun.gif")                 # Image物件
btn = Button(root,image=sunGif,command=msgShow)     # 含影像的按鈕
label.pack()                      
btn.pack()

root.mainloop()

# %%
from tkinter import *

def msgShow():
    label.config(text="I love Python",bg="lightyellow",fg="blue")
      
root = Tk()
root.title("ch4_7")                                 # 視窗標題
label = Label(root)                                 # 標籤內容

sunGif = PhotoImage(file="sun.gif")                 # Image物件
btn = Button(root,image=sunGif,command=msgShow,     # 含文字與影像的按鈕
             text="Click Me",compound=TOP)          
label.pack()                      
btn.pack()

root.mainloop()


# %%

from tkinter import *

def msgShow():
    label.config(text="I love Python",bg="lightyellow",fg="blue")
      
root = Tk()
root.title("ch4_8")                                  # 視窗標題
label = Label(root)                                 # 標籤內容

sunGif = PhotoImage(file="sun.gif")                 # Image物件
btn = Button(root,image=sunGif,command=msgShow,     # 含文字與影像的按鈕
             text="Click Me",compound=CENTER)          
label.pack()                      
btn.pack()

root.mainloop()

#%%
from tkinter import *

def msgShow():
    label.config(text="I love Python",bg="lightyellow",fg="blue")
      
root = Tk()
root.title("ch4_9")                                  # 視窗標題
label = Label(root)                                 # 標籤內容

sunGif = PhotoImage(file="sun.gif")                 # Image物件
btn = Button(root,image=sunGif,command=msgShow,     # 含文字與影像的按鈕
             text="Click Me",compound=LEFT)          
label.pack()                      
btn.pack()

root.mainloop()




# %%

# ch4_10.py
from tkinter import *

root = Tk()

root.title("ch4_10")                                # 視窗標題
lab  = Label(root,text="",bg="yellow",width=20)
btn7 = Button(root,text="7",width=3)
btn8 = Button(root,text="8",width=3)
btn9 = Button(root,text="9",width=3)
btnM = Button(root,text="*",width=3)                # 乘法符號
btn4 = Button(root,text="4",width=3)
btn5 = Button(root,text="5",width=3)
btn6 = Button(root,text="6",width=3)
btnS = Button(root,text="-",width=3)                # 減法符號
btn1 = Button(root,text="1",width=3)
btn2 = Button(root,text="2",width=3)
btn3 = Button(root,text="3",width=3)
btnP = Button(root,text="+",width=3)                # 加法符號
btn0 = Button(root,text="0",width=8)
btnD = Button(root,text=".",width=3)                # 小數點符號
btnE = Button(root,text="=",width=3)                # 等號符號

lab.grid(row=0,column=0,columnspan=4)
btn7.grid(row=1,column=0,padx=5)
btn8.grid(row=1,column=1,padx=5)
btn9.grid(row=1,column=2,padx=5)
btnM.grid(row=1,column=3,padx=5)                    # 乘法符號
btn4.grid(row=2,column=0,padx=5)
btn5.grid(row=2,column=1,padx=5)
btn6.grid(row=2,column=2,padx=5)
btnS.grid(row=2,column=3,padx=5)                    # 減法符號
btn1.grid(row=3,column=0,padx=5)
btn2.grid(row=3,column=1,padx=5)
btn3.grid(row=3,column=2,padx=5)
btnP.grid(row=3,column=3,padx=5)                    # 加法符號
btn0.grid(row=4,column=0,padx=5,columnspan=2)
btnD.grid(row=4,column=2,padx=5)                    # 小數點符號
btnE.grid(row=4,column=3,padx=5)                    # 等號符號

root.mainloop()









# %%
from tkinter import *

def msgShow():
    label.config(text="I love Python",bg="lightyellow",fg="blue")
      
root = Tk()
root.title("ch4_11")                                # 視窗標題

label = Label(root)                                 # 標籤內容

sunGif = PhotoImage(file="sun.gif")                 # Image物件
btn = Button(root,image=sunGif,command=msgShow,     # 含影像的按鈕
             cursor="star")                         # star外形   
label.pack()                      
btn.pack()

root.mainloop()



# %%



# %%



# %%



# %%



# %%




# %%



# %%



# %%




# %%



# %%



# %%



# %%



# %%



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
