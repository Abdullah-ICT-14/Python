import numpy
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x=numpy.percentile(ages,75)
y=numpy.percentile(ages,90)
z=numpy.percentile(ages,50)
f=numpy.percentile(ages,25)
print('percentile is:',x)
print('percentile is:',y)
print('percentiles is:',z)
print('percentiles is:',f)