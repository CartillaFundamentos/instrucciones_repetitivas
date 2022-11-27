# Ejercicio No. 49: Secuencia de potencias

s = "Serie: "

# input
n = int(input("Número de elementos: "))

# processing
for i in range(1, n+1):
    if i < n:
        s = s + str(i**2) + ","
    else:
        s = s + str(i**2)

# output
print(s)