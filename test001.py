# %%
import numpy as np
import numpy as np
from pathlib import Path
import django
while True:
    pw = 1234
    if pw == 1234:
        pw1 = int(input('請輸入密碼:\t'))
        if pw != pw1:
            print("密碼錯誤！\n")
            pw = pw1
        else:
            print("密碼正確！\n")
            break

while True:
    print("\n正確，歡迎光臨！\n")
    art = int(input('請輸入國文成績: \t'))
    math = int(input('請輸入數學成績:\t'))
    eng = int(input('請輸入英文成績:\t'))
    if art < 0 or math < 0 or eng < 0:
        print("wrong number  重新輸入")
    elif art > 100 or math > 100 or eng > 100:
        print("wrong number  重新輸入")
    else:
        sum = math + eng + art
        avg = sum / 3
        break

print(f"成績總分:{sum:10d},平均成績:{avg:15.3f}")


# %%

squares = []
for i in range(10):
    squares.append(i**2)

print(squares)

print([i**2 for i in range(10)])
# %%

# import django
django.__version__

# %%
#from pathlib import Path

Path('spam')/'bacon'/'eggs'

# 一樣

# open(Path('C:\\')/'Users'/'AI'/'Desktop'/'spam.py')
# open(r'C:\Users\AI\Desktop\spam.py')

Path.home()  # 家目錄
# %%
# %%
x, y = True, False

print(not x and y or x)

# %%
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

indices = np.array(
    [[False, False, True], [False, False, False], [True, True, False]])

print(a[indices])
