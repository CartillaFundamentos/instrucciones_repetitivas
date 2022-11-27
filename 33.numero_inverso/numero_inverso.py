# Ejercicio No. 33: Número en orden inverso.

inverso = 0

# input
num = int(input("Digite un número: "))

# processing
while num > 0:
    inverso = inverso*10 + num%10
    num = num//10

# output
print(inverso)