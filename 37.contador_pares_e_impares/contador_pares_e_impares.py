pares = 0
impares = 0

for i in range(100):
    x = int(input("Digite un número: "))
    if x % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares:", pares)
print("Impares:", impares)