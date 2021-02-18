num=int(input('Enter a range number:\n'))
n=int(input('Give a number:\n'))
a=[]
for i in range(1,num+1):
    if i%n==0:
        a.append(i)

print(min(a))
print(a[0])
