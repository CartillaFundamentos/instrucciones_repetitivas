# Ejercicio No. 38: Múltiplos de 7 y 9 entre 1000 y 5000.

m7 = 0
m9 = 0

# processing
for i in range(1000, 5001):
    if i % 7 == 0:
        m7 += 1
    if i % 9 == 0:
        m9 += 1

# output
print("Multiplos de 7:", m7)
print("Multiplos de 9:", m9)