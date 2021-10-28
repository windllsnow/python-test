#%%





# %%

# %%

# %%
#2-1 微積分
import matplotlib.pyplot as plt
alchol=58
for x in range(0,11):
    if x>0:
        alchol*=0.5
    print(f"當x={x:2d},酒精濃度={alchol}")



# %%
import matplotlib.pyplot as plt
alchol=58
x=[x for x in range(0,11)]
y=[alchol*(1/2)**y for y in x]
plt.axis([0,12,0,60])
plt.plot(x,y)
plt.xlabel("Times")
plt.ylabel("Alcohol concentration")
plt.grid()
plt.show()
# %%
import matplotlib.pyplot as plt
x=[x for x in range(1,101)]
y=[1/y for y in x]
plt.axis([0,100,0,2])
plt.plot(x,y)
plt.xlabel("n")
plt.ylabel("y")
plt.grid()
plt.show()

# %%
import  matplotlib.pyplot as plt 
import numpy as np
x=np.linspace(1,0.01,101)
y=[1/y for y in x]
plt.axis([0,1,0,101])
plt.plot(x,y)
plt.plot(x[100],y[100],'-o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
# %%

# %%

# %%

# %%
