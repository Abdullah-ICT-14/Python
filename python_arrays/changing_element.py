from array import *
arrayName=array('i',[2,4,6,8])

print(arrayName)
arrayName[2]=0
print(arrayName)
print(arrayName[0:2])

arrayName[0:2]=array('i',[1,8,9])
print(arrayName)