# Ejercicio No. 22: Contador de vocales.

frase = input("Ingrese una frase: ")
base = "aeiouAEIOU"
num_vocales = 0
for i in frase:
    if i in base:
        num_vocales += 1
