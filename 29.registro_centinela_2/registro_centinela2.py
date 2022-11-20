# Ejercicio No. 29: Registro centinela 2.

# input
num = int(input("Ingrese un número: "))
pares = 0
impares = 0

# processing
while num != 0:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    num = int(input("Ingrese un número: "))

# output
print("Cantidad de pares: ", pares)
print("Cantidad de impares: ", impares)