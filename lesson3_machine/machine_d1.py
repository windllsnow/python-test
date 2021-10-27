#%%

#預載  

# conda update --all
# conda install -c conda-forge tesseract
# conda install -c conda-forge pytesseract
# conda install -c conda-forge imutils
# conda install opencv
# conda install tensorflow


#%%

import decimal
from tkinter.constants import N
import cv2
img=cv2.imread(r'd:\tmp\license_plate.jpg')
print(type(img),img.shape)
img=cv2.imread(r'd:\tmp\license_plate.jpg',cv2.IMREAD_GRAYSCALE)
print(type(img),img.shape)

import numpy as np 
print("OK")

#%%

l=[1,'A']
print(l)
import numpy as np
arr=np.array([1,"A"])
print(arr)




#%%
for x in range(1,10,2):
    print(x)

print("_"*20)
import numpy as np
for x in np.arange(1,10,2):
    print(x)
#%%

a=0.1+0.1
a1=0.1+0.1+0.1
b=0.2
c=0.3
print(a==b)
print(a1==c)


# %%
import numpy as np
for x in np.arange(1,10,0.2):
    print(x)

# %%
import numpy as np
from decimal import*
start=decimal.Decimal('1')
stop=decimal.Decimal('10')
step=decimal.Decimal("0.2")
for y in np.arange(start=start,stop=stop):
    print(y,type(y))

for y in np.arange(1,10,0.2):
    print(y)
# %%
import numpy as np
arr=np.array([1,2])
print(arr.dtype)
z=arr+255
print(z,type(z))



arr=np.array([1,2],dtype='uint8')
print(arr.dtype)
z=arr+255
print(z,type(z))


# %%

import numpy as np
arr=np.array([1,2,3],dtype='int32')
print(arr.dtype)
print(arr.itemsize)
print(arr.nbytes)
# %%
a=[1,2]
b=[4,5]
c=a+b
print(c)
import numpy as np
a=np.array([1,2])
b=np.array([4,5])
c=a+b
print(c)


# %%
l=range(1,10)
l=[x**2 for x in l ]
print(l)
print(type(l))

import numpy as np
l=np.arange(1,10)
l=l**2
print(l)
print(type(l))

# %%
element=np.unique([1,2,3])
print(element)
a=np.unique(list("Michael"))
print(a)
print(a.size)


b=np.unique(list("Victor"))
print(b)
print(b.size)


print(np.intersect1d(a,b).size/np.union1d(a,b).size)   #   --->2/11

# %%



# %%



# %%


# %%



# %%


