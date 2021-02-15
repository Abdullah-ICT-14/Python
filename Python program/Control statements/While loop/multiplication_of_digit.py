number=int(input('Enter a number:\n'))

mul=1
while number>0:
    digit=number%10

    mul=mul*digit
    number=number//10
print(mul)