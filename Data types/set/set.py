firstset={ 1,2,38,4,5,7}
print(type(firstset))
for x in firstset:
      print(x)
if 6 in firstset:
     print(True)
else:
     print(False)

firstset.add(9)
firstset.update('10','11','12')
print(firstset)
print(len(firstset))
firstset.remove(38)


firstset2={ 12,13,14}
add=firstset.union(firstset2)
print(add)

sett=set((1,2,3,4,5))
print(sett)
setter=sett.union(add)
print(setter)
dis=firstset.difference(sett)
print(dis)