#by using + operator
mylist=['abdullah',15,'ruma','tayeba','tamanna']
mylist.append('aysa')
mylist.insert(3,'abdullah')
mylist.pop(4)
print(mylist)
mylist.remove('ruma')
print(mylist)
for x in mylist:
    print(x)
del mylist[0]
print(mylist)
thislist=list(mylist)
add=mylist+thislist
print(add)

hellolist=list(('zaber','sohag','shourob'))

print(hellolist)


