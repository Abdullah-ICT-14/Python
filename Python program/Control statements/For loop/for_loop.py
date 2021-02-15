data=[1,2,3,4,5]
print(sum(data))
for i in data:
    print(i)

for x in 'abdullah':
    print(x)

for j in ['abdullah','ruma',23,18]:
    print(j)

for x in range(2,100,1):
    if x%2==0:
        print('even',x)
        if x==8:
            break
    else:
        print('odd',x)

for x in range(100, 1, -1):
    if x % 2 == 0:
        print('even', x)
        if x==96:
            break
    else:
        print('odd', x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
 pass


n=int(input('Enter any number to print sequnece:\n'))
i=int(input("initial number of the sequence:\n"))
d=int(input('Enter increment or decrement number:\n'))
for x in range(i,n,d):
    print('%d x %d = %d'%(x,x,x*x))