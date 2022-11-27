# Ejercicio No. 26: Cajero de banco.

diez_mil = 0
dos_mil = 0
cien = 0

cheque = int(input("Valor del cheque: ")) # input

# processing
while cheque != 0:
    while cheque > 10000:
        cheque -= 10000
        diez_mil += 1
    while cheque > 2000:
        cheque -= 2000
        dos_mil += 1
    while cheque > 0:
        cheque -= 100
        cien += 1
    cheque = int(input("Valor del cheque: ")) # input

# output
print("Billetes de $10000 gastados:", diez_mil)
print("Billetes de $2000 gastados:", dos_mil)
print("Monedas de $100 gastadas:", cien)