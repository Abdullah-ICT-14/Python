num=int(input('Enter a number to check palindrome:\n'))
temp=num
count=0
sum=0
while num>0:
    digit=num%10
    num=num//10
    sum=sum*10
    sum=sum+digit
    count=count+1
print(sum)
if temp==sum:
    print('is palindrome')
else:
    print('not palindrome')
print(count)