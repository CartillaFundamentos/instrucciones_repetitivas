# Ejercicio No. 32: Sumar los dígitos de un número

suma = 0

# input
num = int(input("Digite un número: "))

# processing
while num > 0:
    suma += num % 10
    num = num // 10

# output
print("El resultado de la suma es:", suma)