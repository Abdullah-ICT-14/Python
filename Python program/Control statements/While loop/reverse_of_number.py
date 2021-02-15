number=int(input('Enter a number:\n'))
sum=0
while number>0:
    digit=number%10
    number=number//10
    sum=sum*10
    sum=sum+digit
print('Reverse of a number is:',sum)
