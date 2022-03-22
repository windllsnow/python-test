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
#%%
employee = {'Alice' : 10000,
            'Bob' : 99817,
            'Carol' : 122990,
            'Frank' : 88123}


top = []
for key , val in employee.items():
    if val >=100000:
        top.append((key,val))
print(top)


print("\n")

top1 = [(k,v) for k, v in employee.items() if v >=100000] 
print(top1)
#%%



#[表達式 + 條件式]
[x * 2 for x in range(5)]
print([(x,y) for x in range(5) for y in range(3)])
print([x **2  for x  in range(10) if x % 2 >0 ])
print([x.lower() for x in ['I','AM','NOT','SHOUTING']])



#%%
