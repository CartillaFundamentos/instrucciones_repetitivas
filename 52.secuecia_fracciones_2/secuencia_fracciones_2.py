# Ejercicio No 52: secuencia de fracciones 2.

s = "Serie: "

# input
n = int(input("Número de elementos: "))

# processing
for i in range(1, n+1):
    if i < n:
        s = s + "1/" + str(i**2 + 1) + ","
    else:
        s = s + "1/" + str(i**2 + 1)

# output
print(s)