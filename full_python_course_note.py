

friends = ["alld", "dsd", "dkkd", "fsad"]
best_friend = "alld"


for friend in friends:
    if friend == best_friend:
        print(f"{best_friend}  is in friends ,I got you")

# %%
budget = 100

sandwich = 5

for s in range(19):  # 0~18
    print(f"you bopught a sandwich. ")
    budget -= sandwich
print(budget)
# %%
budget = 100
sandwich = 5

while True:
    print(f"you bopught a sandwich. ")
    budget -= sandwich
    if budget == 0:
        break
print(budget)

# %%
# Elevator Program

while True:

    answer = int(input("key"))
    if answer == "out":
        print("Exiting")
        break
    else:
        if answer > 0 and answer <= 10:
            print(answer)
        else:
            print(f"{answer}  is over")
            print("bye bye")
            break

# %%


def special_count(stop, step):
    for i in range(1, stop+1, step):
        print(f"Special count{i}")


special_count(5, 1)

# %%
# 勾股定理


def is_pyth_triple(a, b, c):
    num_ab = a**2+b**2
    num_c = c**2
    if num_ab == num_c:
        print(f"The conbination of : {a},{b},{c} supports pyth law!")
    else:
        print(f"The combination of:{a},{b},{c} doesn't")


is_pyth_triple(3, 4, 5)
is_pyth_triple(12, 13, 15)
is_pyth_triple(7, 24, 25)
# %%


def square_my_number(num):
    result = (num**2)

    return print(f"hi+{result}")


square_my_number(9)

# %%


# %%
def numbers(max):
    sum = 0
    for n in range(1, max+1):
        sum += n
    return sum


value = numbers(int(input("請輸入你希望運算從 1 加總到幾的數字： ")))
# 因為這時候輸入的數字是字串，記得加入 int 把字串變成浮點數
print(value)

# %%


# %%


# %%


# %%
