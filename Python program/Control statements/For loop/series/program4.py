#1^2+2^2+3^2+4^2+5^2+....+N^2=?
num=int(input('Enter any number:\n'))
sum=0
for x in range(1,num+1,1):
    sum=sum+x*x
print('result is:',sum)