

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





 
# %%
