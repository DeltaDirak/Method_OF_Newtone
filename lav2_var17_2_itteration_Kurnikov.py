from math import tan
# Нахождения корня методом иттераций
E = float(input()) # Погрешность 
x = float(input()) # Начальное приближение
y = 10
k = 0
while abs(y)>E:
    d = (tan(x))**3+1
    y = d - x
    x = d
    k = k + 1
print('Корень', x)
print('Числе иттераций',k)
print('Проверка',-x+(tan(x))**3+1)