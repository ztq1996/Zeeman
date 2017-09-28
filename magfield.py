'''
Created on Sep 28, 2017

@author: zhangtianqing
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
print 'successfully import'

def linear(x,a,b):
    return a*x+b



Center_increse=[[0, 250.8], [1, 489.5], [2, 879.8], [3,1271.5], [4, 1671.4], [5, 2152.8], [6, 2620.4], [7, 3136.6], [8, 3438.7], [9, 3861.3], [10, 4312.6], [11, 4720.1], [12, 5139], [13, 5569], [14, 5962.8], [15, 6376.3], [16, 6761.5], [17, 7115], [18, 7467.1], [19, 7800.7], [20.0, 8106.4]]
Center_increse=np.asarray(Center_increse).T.tolist()
Edge_increse=[[0, 232.2], [1, 524.1], [2, 810.0], [3, 1144.7], [4, 1528.4], [5, 1955.3], [6, 2293.9], [7, 2746.8], [8, 3101.2], [9, 3464.9], [10, 3833.3], [11, 4273.6], [12, 4653.2], [13, 4973.3], [14, 5301.1], [15, 5598.0], [16, 5930.0], [17, 6264.7], [18, 6620.1], [19, 6858.8], [20, 7147.3]]
Edge_increse=np.asarray(Edge_increse).T.tolist()


popt1,pcov1=curve_fit(linear, Center_increse[0],Center_increse[1])
x1=[i for i in range(21)]
y1=[]
for i in x1:
    y1.append(linear(i,*popt1))
 
popt2,pcov2=curve_fit(linear, Edge_increse[0],Edge_increse[1])
x2=[i for i in range(21)]
y2=[]
for i in x2:
    y2.append(linear(i,*popt2))

plt.plot(Center_increse[0],Center_increse[1],'o')
plt.plot(x1,y1,'r-',label='center')
plt.plot(Edge_increse[0],Edge_increse[1],'o')
plt.plot(x2,y2,'b-',label='edge')
plt.xlabel('Voltage (V)')
plt.ylabel('Magnetic Field (Gauss)')
plt.legend()
plt.show()

meanfield=[]
meanfielderror=[]
voltage=[]
for i in range(len(Center_increse[0])):
    voltage.append(Center_increse[0][i])
    average=(Center_increse[1][i]+Edge_increse[1][i])/2
    error=abs(Center_increse[1][i]-Edge_increse[1][i])/2
    meanfield.append(average)
    meanfielderror.append(error)
 
popt3,pcov3=curve_fit(linear, voltage,meanfield)
x3=[i for i in range(21)]
y3=[]
for i in x3:
    y3.append(linear(i,*popt3))  

plt.plot(Center_increse[0],Center_increse[1],'o')
#plt.plot(x1,y1,'r-',label='Center')

plt.plot(Edge_increse[0],Edge_increse[1],'o')
#plt.plot(x2,y2,'b-',label='Edge')

plt.xlabel('Voltage (V)')
plt.ylabel('Magnetic Field (Gauss)')

plt.errorbar(voltage, meanfield, meanfielderror,fmt='o')
plt.plot(x3,y3,'b-',label='Combined')

plt.legend()
plt.show()



