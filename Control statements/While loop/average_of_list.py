num=int(input('Enter number of element in list:\n'))
a=[]
i=1
while i<=num:
    element=int(input('Enter the list value %d:\n'%i))
    a.append(element)
    i=i+1
y=sum(a)
print('summation is:',y)
avg=sum(a)/num
print('average value is:',avg)
print( 'maximum value is:',max(a))
print('minimum value is:',min(a))