
fibo=int(input('Enter a number  that you want too find a series:\n'))
first_number=0
second_number=1
print(first_number)
print(second_number)
for i in range(1,fibo):
   third_number=first_number+second_number
   first_number=second_number
   second_number=third_number
   print(third_number)