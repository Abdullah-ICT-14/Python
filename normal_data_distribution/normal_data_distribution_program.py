import  numpy
import matplotlib.pyplot as plt
x=numpy.random.normal(5.0,0.1,1000)
print(x,end='')
plt.hist(x,100)
plt.show()
