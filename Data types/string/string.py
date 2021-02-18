"""
String literals in python are surrounded by either single quotation marks, or double
quotation marks.
"""
print('hello')
print("hello")

"""
Assign String to a Variable
"""
a='hello'
print(a)

#You can assign a multiline string to a variable by using three quotes:

b="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua
"""
print(b)
print(b[0])
#You can return a range of characters by using the slice syntax.
print(b[2:10])

#Use negative indexes to start the slice from the end of the string:

print(b[-10:-2])

#To get the length of a string, use the len() function.

print(len(b))
#The strip() method removes any whitespace from the beginning or the end:
print(b.strip())

#The lower() method returns the string in lower case:
x='HELLO'
print(x.lower())
print(x.casefold())#To check if a certain phrase or character is present in a string, we can use the
#keywords in or not in .

u='hello'
print(u.upper()) #The lower() method returns the string in lower case:

print(u.replace('h','j'))#The replace() method replaces a string with another string:

#The split() method splits the string into substrings if it finds instances of the
#separator:
print(b.split())


#To check if a certain phrase or character is present in a string, we can use the
#keywords in or not in .

txt ='hello how are you i am fine'
p='am' in txt
q='am' not in txt
print(p)
print(q)

#To concatenate, or combine, two strings you can use the + operator.
ar='i'
br='love'
cr='you'
dr=ar+br+cr
print(dr)

#To add a space between them, add a " " :
cct=ar+' '+ br +' '+cr
print(cct)

#we can combine strings and numbers by using the format() method!
#The format() method takes the passed arguments, formats them, and places them
#in the string where the placeholders {} are:
"""
pp='i am abdullah'
oo=23
ppp=pp+oo   #give an error because oo is not string and we can't add string andd number

"""
oo=23
text= "i am abdullah and  i am { }"
print(text.format(oo))