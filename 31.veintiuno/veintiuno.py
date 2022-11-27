# Ejercicio No. 31: Veintiuno.

from random import randint

j = 0
d = 0

# el dealer toma dos cartas y una se le muestra al jugador
m = randint(1, 12)
d += m
print("Una de las dos cartas del dealer vale", m)
m = randint(1, 12)
d += m

# el jugador recibe una carta
m = randint(1, 12)
j += m

print("Su suma es:", j)

# input
seguir = int(input("Digite 1 para continuar o 0 para plantarse: "))

# processing
while seguir == 1 and j < 22:
    m = randint(1, 12)
    j += m
    print("Su suma es:", j)
    seguir = int(input("Digite 1 para continuar o 0 para plantarse: "))

while d < 17: # el dealer intenta acercarse al 21
    m = randint(1, 12)
    d += m

# output
if d > 21 and j < 22 or j > d and j < 22:
    print("Ganaste, y el dealer tenía una suma de", d)
else:
    print("Perdiste, y el dealer tenía una suma de", d)