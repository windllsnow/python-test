#%%

print("234214")


letters_amazon = '''
We spent several years building our  own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as 
the commercial engines, but at one-tenth of the cost. We were 
not surprised when this worked.
'''

find = lambda x ,q : x[x.find(q)-18:x.find(q) +18] if q in x else -1

print(find(letters_amazon, 'SQL'))
#%%----------------------------------------------------------------

price = [[9.9,9.8,9.8,9.4,9.5,9.7],
        [9.5,9.4,9.4,9.3,9.2,9.1],
        [8.4,7.9,7.9,8.1,8.0,8.0],
        [7.1,5.9,4.8,4.8,4.7,3.9],]
sample = [line[::2] for line in price]
print(sample)




#%%








