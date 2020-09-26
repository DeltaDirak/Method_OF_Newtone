# Нахождение одного корня методом хорд
def f(x):
    return x**4-18*x-10
E = float(input()) # Погрешность 
a = float(input()) # Правая граница
b = float(input()) # Левая граница
n = 0
A = f(a)
B = f(b)
while abs(A)>E and abs(B)>E:
    d = (-b*A+a*B)/(B-A)
    D = f(d)
    if D>0:
        b = d
    else:
        a = d
    n = n + 1
    A = f(a)
    B = f(b)
if abs(B)<abs(A):
    A = B
print('Корень', d)
print('Результат функции', A)
print('Число иттераций', n) 