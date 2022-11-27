# Ejercicio No. 47: Factoriales.

# input
num = int(input("Digite un número: "))

# processing
if num == 0:
    num = 1
else:
    for i in range(1, num):
        num = num * i

# output
print("Su factorial es:", num)