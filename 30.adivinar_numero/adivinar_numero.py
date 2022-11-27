# Ejercicio No. 30: Adivinar un número.

from random import randint
num = randint(0, 100)
intentos = 0

# input
adivino = int(input("Adivina el número: "))

# processing
while adivino != num:
    if adivino < num:
        print("El número es más grande.")
    else:
        print("El número es más pequeño.")
    intentos += 1
    adivino = int(input("Adivina el número: "))

# output
print("¡Ese es el número!")
print("Número de intentos:", intentos)