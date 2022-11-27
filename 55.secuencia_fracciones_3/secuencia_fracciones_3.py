# Ejercicio No. 55: Secuencia de fracciones 3.

s = "Serie: "

# input
n = int(input("Número de elementos: "))

# processing
for i in range(1, n+1):
    if i < n:
        s = s + str(i**(i-1))+ "/" + str(2*i + 1) + ","
    else:
        s = s + str(i**(i-1)) + "/" + str(2*i + 1)

# output
print(s)