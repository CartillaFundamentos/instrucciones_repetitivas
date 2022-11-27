# Ejercicio No. 37: contador de pares e impares.

pares = 0
impares = 0

# processing
for i in range(20):
    num = int(input("Digite un número: ")) # input
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares:", pares) # output
print("Impares:", impares) # output