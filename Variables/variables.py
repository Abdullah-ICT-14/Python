

#Variables do not need to be declared with any particular type and can even change
#type after they have been set.
x=5
y='john'
print(x,y)

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

#String variables can be declared either by using single or double quotes:
v="john"
c='john'
print(v,c)


#Python allows you to assign values to multiple variables in one line:
a,b,c=4,5,6
print(a,b,c)
p,q,r='jo','hn','cena'
print(p,q,r)

#And you can assign the same value to multiple variables in one line:
w=s=t='orange'
print(t)

#To combine both text and a variable, Python uses the + character:
print('python',x)

#Variables that are created outside of a function (as in all of the examples above) are
#known as global variables.
#To create a global variable inside a function, you can use the global keyword.

def myfunc():
    global  kar
    kar='fantastic'
myfunc()
print(kar)


#To change the value of a global variable inside a function, refer to the variable by
#using the global keyword:

jar=5
def jaifun():
    global jar
    jar='john'

jaifun()
print(jar)