#%%
false_values = [
    False,
    [],
    {},
    '',
    0,
    0.0,
    None
]

for value in false_values:
    print(True if value else False)
#%%



print((lambda x : x +3 )(3))

employee = {'Alice' : 10000,
            'Bob' : 99817,
            'Carol' : 122990,
            'Frank' : 88123}


top = []
for key , val in employee.items():
    if val >=100000:
        top.append((key,val))
print(top)


#%%