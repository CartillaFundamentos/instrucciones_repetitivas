# Ejercicio No. 45: Contador de vocales.

num_vocales = 0
base = "aeiouAEIOU"

# input
frase = input("Ingrese una frase: ")

# processing
for i in frase:
    if i in base:
        num_vocales += 1

# output
print("Número de vocales:", num_vocales)