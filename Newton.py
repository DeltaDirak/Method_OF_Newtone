# Метод Ньютона 
from matplotlib import pyplot as plt
import math
import numpy as np

def G(x):
    return (math.tan(x))**3+1

def F(x):
    return (math.tan(x))**3+1-x

def F1(x):
    return 3*(math.tan(x))**2*(1/(math.cos(x)**2))-1

k = 0
E = float(input())
x0 = float(input())
x = []
xx = []
y = []
yy = []
while abs(F(x0))>E:
     x0 = x0 - F(x0)/F1(x0)
     k=+1
print(F(x0))
print(x0)  
print(k)

for i in np.arange(4, 4.2, 0.01):
    x.append(i)
    y.append((math.tan(i))**3+1) 
    xx.append(i)
    yy.append(i) 
plt.plot(x,y,xx,yy)
plt.plot(x0,G(x0),marker= "*",color="red")
plt.show()

