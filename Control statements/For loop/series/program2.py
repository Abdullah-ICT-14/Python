#1+3+5+....+N=?
num=int(input('Enter any number:\n'))
sum=0
for x in range(1,num+1,2):
    sum=sum+x
print(sum)