num1=int(input('Enter a range number:'))
firstnumber=int(input('First number:\n'))
increment=int(input('Enter the increment:\n'))

for i in range(firstnumber,num1+1,increment):
a = []
for j in range(1,i+1):
       print(j, sep=' ', end=' ')
       if i < j:
           print('+', sep=' ', end=' ')
    a.append(j)
print('=',sum(a))
