# Ejercicio No. 35: Inversión para negocio.

meses = 0

# input
c1 = int(input("Capital de Pedro: "))
c2 = int(input("Capital de Juan: "))
c3 = int(input("Inversión para el negocio: "))

# processing
while c1 + c2 < c3:
    meses += 1
    c1 *= 1.03
    c2 *= 1.04

# output
print("Meses requerido:", meses)