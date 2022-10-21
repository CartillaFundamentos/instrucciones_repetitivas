# Ejercicio No.  : Número en orden inverso.

# input
num = int(input("Digite un número: "))
inverso = 0

# processing
while num > 0:
    inverso = inverso * 10 + num % 10
    num = num // 10

# output
print(inverso)