#1+2+3+4+5+....+N=?
num=int(input('Enter any number:\n'))
sum=0
for x in range(1,num+1,1):
    sum=sum+x
print('result is:',sum)