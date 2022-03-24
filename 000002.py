#%%

# Python 不廢話一行程式碼

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
#lambda 參數 : return 表達式

lambda x,y : x+y

txt1= ['lambda functions are anonymous functions.',
        'anonymous function dont  have a name.',
        'functions are objects in Python.']
mark = map (lambda s : ( True, s) if 'anonymous' in s else (False, s), txt1)

print(list(mark))
#%%

text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having little or no money in my purse, and nothing particular to interest me on shore , I thought I would sail about a little and see the watery part of  the world . It is a way I have of driving off the  spleen , and regulating the circulation. - Moby Dick'''

w =[[x for x in line.split() if len (x)>3] for line in text.split('\n')]
print(w)
#%%
#x[start:stop:step]

ss = 'Eat more fruits!'
print(ss[0:3])

print(ss[3:])


print(ss[4:8:2])
print(ss[::-1])
print(ss[6:1:-1])


#%%



# %%

