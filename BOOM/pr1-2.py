import math

def triug(a, b, c):
    #Проверка треугольника
    return a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0

def triugtype(a, b, c):
    #тип треугольника
    if a == b == c:
        return 'Равносторонний'
    if a == b or a == c or b == c:
        return 'Равнобедренный'
    return 'Разносторонний'

def plosh(a, b, c):
    #площадь по формуле Герона
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c))
    return

# Ввод 
while True:
    a = float(input("Введите длину первой стороны: "))
    b = float(input("Введите длину второй стороны: "))
    c = float(input("Введите длину третьей стороны: "))
    
    # проверка существования
    if triug(a, b, c):
        break
    else:
        print("Нет такого трегольника")

# класс треугольника
triugclass= triugtype(a, b, c)
print(f"Тип треугольника: {triugclass}")

# площадь треугольника
s = plosh(a, b, c)
