# Ejercicio No. 44: Sumar con rango ingresado.

suma = 0

# input
n = int(input("Digite el valor de n: "))

# processing
for i in range(1, n+1):
    suma += i

# output
print("Suma desde 1 hasta n:", suma)