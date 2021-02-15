#1^5+2^5+3^5+4^5+5^5+....+N^5=?
num=int(input('Enter any number:\n'))
sum=0
for x in range(1,num+1,1):
    sum=sum+pow(x,5)
print('result is:',sum)