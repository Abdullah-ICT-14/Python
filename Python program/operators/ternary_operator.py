al=10
b=5
print(al) if al>b else print(b)

c=al if al>b else b
print(c)

dd=[5,1,3,2,4]
print(dd)
dd[3]='string'
print(dd *3)
print(len(dd))
dd.append(6)
print(dd)
dd.insert(5,'five')
print(dd)
dd.remove('five')
dd.pop(3)
dd.sort()
print(dd)
dd.reverse()
print(dd)
aa=dd.copy()
print(aa)
print(aa.index(4))
print(aa.count(1))