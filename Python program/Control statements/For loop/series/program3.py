#5+10+15+....+N=?
num=int(input('Enter any number:\n'))
sum=0
for x in range(5,num+1,5):
    #print(x)
    sum=sum+x
    #print(sum)
print(sum)