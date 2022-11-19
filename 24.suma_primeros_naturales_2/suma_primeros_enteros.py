# Ejercicio No. 24: Suma de los n primeros números naturales 2

# input
n = int(input("Ingrese el valor de n: "))

# processing
i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

# output
print("La suma de los", n, "primeros números es:", sum)