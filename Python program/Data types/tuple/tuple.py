thisTuple=(1,2,3,5)
print(thisTuple)
print(thisTuple[0])
print(thisTuple[-1])
print(thisTuple[1:3])
print(thisTuple[-3:-2])
convertTuple=list(thisTuple)
convertTuple[1]='hello'
thisTuple=tuple(convertTuple)
print(thisTuple)
for x in thisTuple:
    print(x)

if 2 in thisTuple:
    print(True)

print(len(thisTuple))
oneitem=(1,)
del oneitem
print(thisTuple.count(5))