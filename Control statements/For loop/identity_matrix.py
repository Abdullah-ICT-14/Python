num=int(input('Enter raw and coloumn number:'))
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==j:
            print('1',end=' ')
        else:
         print('0',end=' ')
    print()