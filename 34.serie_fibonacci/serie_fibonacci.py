a = 0
b = 1

suma = a + b
a = b
b = suma

while suma < 900:
    suma = a + b
    a = b
    b = suma
    print(suma)