print(10>9)
print(10==9)
print(10<9)

#When you run a condition in an if statement, Python returns True or False :
if 10>9:
    print('10 is greater than 9')
else:
    print('9 is less than 10')

#The bool() function allows you to evaluate any value, and give you True or False
print(bool('15'))
print(bool(15))

x='hello'
y=15
print(bool(x))
print(bool(y))


#Almost any value is evaluated to True if it has some sort of content.


"""
In fact, there are not many values that evaluates to False , except empty values,
such as () , [] , {} , "" , the number 0 , and the value None . And of course the
value False evaluates to False .
"""
print(bool(False))
print(bool(None))
print(bool([]))

#Functions can Return a Boolean
def myfunction():
    return  True
print(myfunction())

#isinstance() function, which can be used to determine if an object is of a certain
#data type:
x=15
print(isinstance(x,int))