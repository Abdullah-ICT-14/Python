def table(n):
    return lambda b:b*n

n=int(input('\n'))
b=table(n)
for i in range(1,11):
    print(n,'X',i,'=',b(i))