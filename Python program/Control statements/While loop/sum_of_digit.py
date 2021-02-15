number=int(input('Enter a number:\n'))
sum=0
mul=1
while number>0:
    digit=number%10
    sum=sum+digit
    mul=mul*digit
    number=number//10
print(sum)