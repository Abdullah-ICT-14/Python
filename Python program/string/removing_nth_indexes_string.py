def remove(string,n):
    first=string[:n]
    print(first)
    last=string[n+1:]
    print(last)
    return first+last
string=str(input('Enter a string:\n'))
n=int(input('enter index:\n'))
print(remove(string,n))
