import matplotlib.pyplot as plt 

values=[16,18,4]
labels=['python','ruby','java']
piexplode=[0.4,0,0]
plt.pie(values,labels=labels,startangle=90,shadow=True,explode=piexplode)

plt.title('pie chart')

plt.xlabel('horizontal title')

plt.ylabel('verticle title')
plt.legend(loc='best')
plt.show()