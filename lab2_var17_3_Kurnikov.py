# Задание три
# Метод Ньютона для решений системы нелинейных уравнений (2 уравнения)
from matplotlib import pyplot as plt
from math import sin,cos
import numpy as np

def F1(x,y):
    return sin(x+1)-1-y

def F2(x,y):
    return 2*x+cos(y)-2

# Первые производные
def F1dx(x,y):
    return cos(x+1)

def F1dy(x,y):
    return -1

def F2dx(x,y):
    return 2

def F2dy(x,y):
    return -sin(y)

E = float(input()) # Error
x = float(input()) # initial approximtion
y = float(input())
f1 = F1(x,y)
f2 = F2(x,y)
N = f1-f2
k = 0
while abs(N)>E:
    
    a11 = F1dx(x,y)
    a12 = F2dx(x,y)
    a21 = F1dy(x,y)
    a22 = F2dy(x,y)
    d = a11*a22-a12*a21
    # inverse matrix compilation
    if d != 0:
        A11 = a11/d
        A12 = -a21/d
        A21 = -a12/d
        A22 = a22/d
    # additives
    dx = (A11*f1+A21*f2)
    dy = (A12*f1+A22*f2)
    X = x + dx
    Y = y + dy
    f1 = F1(X,Y)
    f2 = F2(X,Y)
    #N = (dx**2-dy**2)**(0.5)
    N = (abs(f1**2-f2**2))**(0.5)
    x = X
    y = Y
    k+=1
print('Значение по оси абсцисс',x,'Значение по оси ординат',y) # solution of the equation
print('Число иттераций',k) # number of iteration

# Graphic solution
x = []
y = []
xx = []
yy = []
for i in np.arange(-5, 5, 0.01):
    x.append(i)
    y.append(sin(i+1)-1) 
for j in np.arange(-5, 5, 0.01):
     yy.append(j)
     xx.append(1-cos(j)/2) 
plt.plot(x,y,xx,yy)
plt.show() 
