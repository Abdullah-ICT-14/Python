string1=str(input('Enter a string:\n'))
count=0
count2=0
for i in string1:
    if i.isdigit():
        count += 1
     #count+=1
    count2=count2+1
print(count)
print(count2)