import matplotlib.pyplot as plt 
x1=[1,2,3,4,5]
x2=[1,2,3,4,5]
x3=[1,9,3,2,8]
y1=[1,2,4,8,16]
y2=[1,3,9,13,16]
y3=[1,3,4,5,6]
plt.plot(x1,y1 ,'ro-',label='line 1')
plt.plot(x2,y2,'bo--',label='line 2')
plt.plot(x3,y3,'g^-',label='line 3')
plt.legend(loc='best')
#plt.plot(<X axis values>,<y values>,'line type')
plt.title("harichselvam")
plt.xlabel("Horizontal title")
plt.ylabel("Vertical title")
plt.show()