# Ejercicio No. 26: Rebotes de pelota.

# input
h = int(input("Ingrese la altura inicial de la pelota: "))
quinta = h / 5
rebotes = 0

# processing
while h > quinta:
    h -= h*0.1
    rebotes += 1

# output
print("Número de rebotes:", rebotes)