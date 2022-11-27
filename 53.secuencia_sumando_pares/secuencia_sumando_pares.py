# Ejercicio No. 53: Secuencia sumando pares

s = "Serie: "

# input
n = int(input("Número de elementos: "))

# processing
for i in range(1, n+1):
    if i < n:
        s = s + str(i**2 + i) + ","
    else:
        s = s + str(i**2 + i)

# output
print(s)