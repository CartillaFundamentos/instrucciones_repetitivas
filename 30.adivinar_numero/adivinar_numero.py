# Ejercicio No. 31: Adivinar un número.

import random
number = random.randint(0, 100)

# input
attemp = int(input("Adivine el número: "))

# processing
while attemp != number:
    if attemp > number:
        print("El número es más grande.")
    else:
        print("El número es más pequeño.")
    attemp = int(input("Adivine el número: "))

# output
print("¡Ese es el número!")