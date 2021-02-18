mydic ={ 'name':'abdullah','id':'it-17015','year':'3rd','sem':'2nd'}
print(mydic)
x=mydic['year']
print(x)
y=mydic.get('sem')
print(y)
mydic['year']='4th'
print(mydic)

for p in mydic:
    print(p)
for z in mydic:
    print(mydic[z])
for q in mydic.values():
    print(q)
for r in mydic.items():
    print(r)

if '3rd' in mydic:
    print('yes')
else:
    print('no')

print(len(mydic))

mydic['hall']='jamh'
print(mydic)

mydic.pop('hall')
print(mydic)

mydic.popitem()
print(mydic)

del mydic['name']
print(mydic)

newdic={ 'father':'rahim','mother':'johura','brother':'alauddin'}

newdic=mydic.copy()
print(newdic)
mydic=dict(newdic)
print(mydic)

myfamily={
    'child1':{
    'name':'tamim',
    'age':9
},
    'child2':{
        'name':'tamanna',
        'age':5
    },
    'child':{
        'name':'tayeba',
        'age':10
    }
}

print(myfamily)
