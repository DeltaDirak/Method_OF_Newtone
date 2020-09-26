# Нахождение одного корня методом дихотомии
def f(x):
    return x**4-18*x-10
E = float(input()) # Погрешность 
a = float(input()) # Правая граница
b = float(input()) # Левая граница
n = 0
A = f(a)
B = f(b)
while abs(A-B)>E:
    d = (a+b)/2
    D = f(d)
    if D>0:
        b = d
    else:
        a = d
    n = n + 1
    A = f(a)
    B = f(b)
print('Корень', d)
print('Результат функции', A)
print('Число иттераций', n) 