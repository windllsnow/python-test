#%%
import cv2
img=cv2.imread(r'd:\444.jpg')
print(type(img),img.shape)
img=cv2.imread(r'd:\444.jpg',cv2.IMREAD_GRAYSCALE)
print(type(img),img.shape)
import numpy as np

print('ok')

# %%

l=[1,'a']
print(l)
import numpy as np

arr = np.array([1,'a'])
print(arr)


for i in arr:
    print(i,type(i))

#%%

for x in range(1,19,2):
    print(x)
print("="*20)
import numpy as np
for x in np.arange(1,17,.2):
    print(x)
# %%

# %%
