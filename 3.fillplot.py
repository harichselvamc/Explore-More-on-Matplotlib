import matplotlib.pyplot as plt 
import numpy as np 
 
x=np.arange(0,10)
print(x)
y=0.05*x*x 
print(y)

plt.ylim(0,5)
plt.plot(x,y)

plt.fill_between(x,y,color='blue')
plt.show()