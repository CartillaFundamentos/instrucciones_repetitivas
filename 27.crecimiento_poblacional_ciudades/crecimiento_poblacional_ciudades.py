# Ejercicio No. 28: Crecimiento poblacional de ciudades.

# variables
year = 1980
a = 3.5
b = 5

# processing
while a < b:
    a *= 1.07
    b *= 1.05
    year += 1

# output
print("Año de rebaso: ", year)