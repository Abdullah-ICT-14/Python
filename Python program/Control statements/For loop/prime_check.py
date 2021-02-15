num=int(input('Enter any number:\n'))
i=1
k=0
while i<=num:
    if num % i ==0:
        k=k+1
        print(k,num%i)
    i=i+1
print(k)
if k<=0:
    print('prime')
else:
    print('not prime')