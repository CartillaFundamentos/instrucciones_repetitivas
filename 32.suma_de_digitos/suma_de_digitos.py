# Ejercicio  : Sumar los dígitos de un número

# input
num = int(input("Digite un número: "))
suma = 0

# processing
while num > 0:
    suma += num % 10
    num = num // 10

# output
print("El resultado de la suma es:", suma)