string1=str(input('Enter a string:\n'))
count=0
for i in string1:
    if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i =='I' or i=='o' or i=='O' or i =='u' or i=='U':
        count+=1
print(count)