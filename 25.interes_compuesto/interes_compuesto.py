# Ejercicio No. 25: Interés compuesto.

# input
capital = int(input("Ingrese el valor del capital: "))

# processing
doble = capital*2
meses = 0

while capital <= doble:
    meses += 1
    capital += capital*0.05

# output
print("El capital se duplicó al cabo de", meses, "meses")