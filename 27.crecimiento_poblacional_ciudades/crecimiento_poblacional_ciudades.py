# Ejercicio No. 27: Crecimiento poblacional de ciudades.

año = 1980
A = 3.5
B = 5

# processing
while A < B:
    A *= 1.07
    B *= 1.05
    año += 1

# output
print("Año de rebaso: ", año)