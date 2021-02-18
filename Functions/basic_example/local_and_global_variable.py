def add(a,b):
    c=a+b
    print('local variable is c ')
    return c
num1=int(input('Enter anu number:\n'))
num2=int(input('Enter anu number:\n'))
print('local variable is num1 and num2')
print(add(num1,num2))