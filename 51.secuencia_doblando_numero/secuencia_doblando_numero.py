# Ejercicio No. 51: Secuencia doblando un número.

s = "Serie: "

# input
n = int(input("Número de elementos: "))

# processing
for i in range(1, n+1):
    if i < n:
        s = s + str(2**(i-1)) + ","
    else:
        s = s + str(2**(i-1))

# output
print(s)