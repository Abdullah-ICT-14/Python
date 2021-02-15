num1=int(input('Enter first number:\n'))
num2=int(input('Enter 2nd number:\n'))
while num1!=0 and num2!=0:
    if num1>num2:
        num1=num1%num2
        print('num1:',num1)
    else:
        num2=num2%num1
        print('num2:',num2)
gcd=num1+num2
print(gcd)
