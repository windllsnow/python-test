# %%
# 類別
class Animals:
    this_is_a_property = {
        'key 1': 'Value'
    }
    this_list = ['Kane', 'Kan', 'Gully']

    def add_name(self, name):
        self.this_list.append(name)
        return self.this_list

    def this_is_method(self):
        print(self.this_list)

    @property  # 只能讀取  不能更改
    def get_gully(self):
        return self.this_list[2]


the_animal = Animals()
the_animal.this_is_method()
gully = the_animal.get_gully
print("The cutest go of all time is", gully)


# %%

class Animal:
    fur_color = "Orange"

    def eat(self):
        pass

    def speak(self):

        print("Raaaaaawwwwrrr")

    def chase(self):
        pass


class Tiger(Animal):

    def speak(self):
        print("They're GREEEEEAATTTTTT")


class HouseCat(Animal):

    fur_color = "black"  # overwrite

    def speak(self):
        print("Meow")


tiger = Tiger()
tiger.speak()

cat = HouseCat()
cat.speak()
print(cat.fur_color)
# %%


class Animal:
    fur_color = "Orange"

    def speak(self):
        raise NotImplementedError()

    def chase(self, animal="Gazelle"):
        print("I'm chasing", animal)

    def eat(self):
        print("eat   aaah")


class HouseCat(Animal):

    def eat(self):
        super().eat()
        print(" they   ttttt")

    def chase(self, animal):
        super().chase(animal)
        print(animal, "was caught")


cat = HouseCat()
cat.chase("mouse ")
# %%

# dunder method


class Animal:

    animal_type = " Unknown "

    def __init__(self, fur_color):

        self.fur_color = fur_color

    def speak(self):
        raise NotImplementedError

    def eat(self):
        print("I am eating youm yum yum ")

    def chase(self, animal="Gazelle"):
        print("I'm chasing", animal)

    def get_fur_color(self):
        print("Getting fur color:", self.fur_color)


class HouseCat(Animal):

    def __init__(self, fur_color):
        super().__init__(fur_color)
        print("Fur color was saved to the calss Object")
        self.animal_type = "House Cat"
        print(self.animal_type)

    def eat(self):
        super().eat()
        print(" they   ttttt")

    def chase(self, animal):
        super().chase(animal)
        print(animal, "was caught")


cat = HouseCat("Gray")
cat.get_fur_color()
cat.chase("mouse ")
# %%


try:
    total = 1 / 0
except Exception:
    total = 0

print(total)
# %%
num = input("what is the number")
try:

    num = int(num)
except Exception:
    num = "unknown"

print(num)
# %%
num1 = input("what is the number1:")
num2 = input("what is the number2:")

try:
    num1 = int(num1)
    num2 = int(num2)
    total = num1 / num2
    print("total=num1/num2=", total)
except ValueError:
    print("num1 or num2 were not a valid number")
except ZeroDivisionError:
    print("num2=0  that's not right")
except Exception as e:
    print("Exception was caught")
    print(type(e))

    num1 = "unknown"
    num2 = "unknown"
# %%

# decorator function (好難理解)


def my_decorator(func):
    def wapper():
        print("Do sth here")
        func()
        print("Original function is finished")
    return wapper


@my_decorator
def myfunc():
    print("My name is Kalob")


myfunc()


# %%
