try:
 a = int(input("Enter a:"))
 b = int(input("Enter b:"))
 c = a/b;
 print("a/b = %d"%c)
except:
 print("can't divide by zero")
else:
 print("Hi I am else block")

 x = -1
 if x < 0:
     raise Exception("Sorry, no numbers below zero")