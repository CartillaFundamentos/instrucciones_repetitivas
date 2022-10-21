from random import randint

n = int(input("¿Cuántas veces se va a lanzar el dado?: "))
c1 = ""
c2 = ""
c3 = ""
c4 = ""
c5 = ""
c6 = ""

for i in range(n):
    cara = randint(1, 7)
    if cara == 1:
        c1 += "▯"
    elif cara == 2:
        c2 += "▯"
    elif cara == 3:
        c3 += "▯"
    elif cara == 4:
        c4 += "▯"
    elif cara == 5:
        c5 += "▯"
    elif cara == 6:
        c6 += "▯"

print("Resultados:")
print("1:", c1)
print("2:", c2)
print("3:", c3)
print("4:", c4)
print("5:", c5)
print("6:", c6)