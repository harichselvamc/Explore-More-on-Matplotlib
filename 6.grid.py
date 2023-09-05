import matplotlib.pyplot as plt 

x1=[1,2,3,4,5]
y1=[1,2,4,8,23]

plt.plot(x1,y1,'ro--',label='students')

plt.legend(loc='best')

plt.title("harichselvam")

plt.xlabel("Horizontal")
plt.ylabel("vertical")
plt.grid(linestyle='--',color='black',axis='x')
plt.show()