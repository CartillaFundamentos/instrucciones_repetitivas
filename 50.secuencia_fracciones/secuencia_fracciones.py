# Ejercicio No. 50: Secuencia de fracciones.

s = "Serie: "

# input
n = int(input("Número de elementos: "))

# processing
for i in range(1, n+1):
    if i < n:
        s = s + "1/" + str(i) + ","
    else:
        s = s + "1/" + str(i)

# output
print(s)