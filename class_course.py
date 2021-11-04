#%%
class Bank():
    title='taipei bank'
    def __init__(self,uname,money):
        self.name=uname
        self.balance=money
    def save_money(self,money):
        self.balance+=money
        print("存款",money,"完成")
    def withdraw_money(self,money):
        self.balance-=money
        print("提款",money,"完成")

    def get_balance(self):
        print(self.name,"目前餘額",self.balance)
hungbank=Bank('hung',100)
hungbank.get_balance()

hungbank.save_money(int(input("存款Input:")))
hungbank.get_balance()

hungbank.withdraw_money(int(input("提款Input:")))
hungbank.get_balance()



#%%
class Animal:
    def fly_(self):
        print("animal fly")
class Bird(Animal):
    def fly(self):
        print("fly")
class Duck(Bird):
    pass

duck = Duck()
duck.fly()
duck.fly_()
# %%
class Animal:
    def eat(self):
        print("Animal eat method is called.")
class Bird:
    def eat_(self):
        print("Bird fly method is called")
class Duck(Animal,Bird):
    pass

duck= Duck()
duck.eat()
duck.eat_()

# %%
class Car():
    def __init__(self,name):
        self.name="Car" + name
    def speed(self,num):
        print(', 時 速 是：',num)
class Bmwcar(Car):
    def skill(self, n   ):
        print(", 技 能是：",n)
class Audicar(Car):
    pass


c=Car('car')
b=Bmwcar('BMW')
a=Audicar('Audi')

print(c.name,end=" ")
c.speed(100)

print(b.name,end=" ")
b.speed(200)
b.skill('抓老鼠')

print(a.name,end=" ")
a.speed(150)



# %%
class Banks():
    def __init__(self,uname):
        self.__name=uname
        self.__balance=0
        self.__title="Taipei Bank"
    def save_money(self,money):
        self.__balance+=money
        print("存款",money,"完成")
    def withdraw_money(self,money):
        self.__balance-=money
        print("提款",money,"完成")
    def get_balance(self):
        print(self.__name.title(),"目前餘額",self.__balance)

class Shilin_Banks(Banks):
    pass

x=input ("Input username: ")


uni_bank=Banks(x)
uni_bank.get_balance()

hungbank=Shilin_Banks(x)
hungbank.save_money(int(input("存多少：")))
hungbank.get_balance()
hungbank.withdraw_money(int(input("提多少：")))
hungbank.get_balance()



# %%

class Person():
    def __init__(self,name):
        self.__name=name
    def get_name(self):                       #  再傳回 
        return self.__name
    def set_name(self,new_name):               # 先設定  
        if len(new_name) >=5:
            self.__name =new_name
        else:
            print("error:名字長度需要大於或者等於5")

p=Person("Tom")
p.set_name("Kitty")   # 先設定  再傳回 
print(p.get_name())
# %%

class Banks():
    def __init__(self,uname):
        self.__name=uname
        self.__balance=0
        self.__title="Taipei Bank"
    def save_money(self,s_money):
        self.__balance+=s_money
        print("存款",s_money,"完成")
    def withdraw_money(self,w_money):
        self.__balance-=w_money
        print("提款",w_money,"完成")
    def get_balance(self):
        print("目前餘額",self.__balance)

pizzabank=Banks('pizza')
print(pizzabank._Banks__name)# 破解了私有屬性(利用 物件名稱._類別名稱__私有屬性)
pizzabank.get_balance()
pizzabank._Banks__balance=1000 # 破解了私有屬性(利用 物件名稱._類別名稱__私有屬性)
pizzabank.get_balance()


# %%





# %%




# %%



# %%



# %%



# %%



# %%



# %%


