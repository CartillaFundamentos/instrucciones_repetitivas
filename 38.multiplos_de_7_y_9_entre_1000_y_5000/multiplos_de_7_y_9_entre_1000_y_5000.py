m7 = 0
m9 = 0

for i in range(1000, 5001):
    if i % 7 == 0:
        m7 += 1
    if i % 9 == 0:
        m9 += 1

print("Multiplos de 7:", m7)
print("Multiplos de 9:", m9)