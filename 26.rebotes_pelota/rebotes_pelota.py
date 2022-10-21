# Ejercicio No. 27: Rebotes de pelota.

# input
h = int(input("Ingrese la altura inicial de la pelota: "))
ah = h
bounces = 0

# processing
while ah > h / 5:
    ah *= 0.9
    bounces += 1

# output
print("Número de rebotes:", bounces)