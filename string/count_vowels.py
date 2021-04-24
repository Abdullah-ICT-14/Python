"""
Program to check vowel
"""
STRING=str(input('Enter a string:\n'))
COUNT=0
for k in STRING:
    if k in('a','A','e','E','i','I','o','O','u','U'):
        COUNT+=1
print(COUNT)
