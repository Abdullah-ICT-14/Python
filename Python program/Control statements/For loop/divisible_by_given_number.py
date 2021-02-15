num=int(input('Enter a range number:\n'))
n=int(input('Give a number:\n'))
for i in range(1,num+1):
    if i%n==0:
        print(i,end=' ')
