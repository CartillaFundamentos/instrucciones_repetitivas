# Ejercicio No. 26: Interés compuesto.

# input
c = int(input("Ingrese el valor del capital: "))

# processing
vc = c
m = 0
while vc < c*2:
    m += 1
    vc += 0.05 * vc

# output
print("El capital se duplicó al cabo de", m, "meses")