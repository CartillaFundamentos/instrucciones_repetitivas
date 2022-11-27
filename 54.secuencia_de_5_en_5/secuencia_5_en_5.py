# Ejercicio No. 54: Secuencia de 5 en 5.

s = "Serie: "

# input
n = int(input("Número de elementos: "))

# processing
for i in range(1, n+1):
    if i < n:
        s = s + str(5*i - 2) + ","
    else:
        s = s + str(5*i - 2)

# output
print(s)