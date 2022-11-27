# Ejercicio No. 48: Buscar número en conjunto.

lista = [1,2,3,4,5]
b = False

# input
numero = int(input("Número a buscar: "))

# processing
for i in lista:
    if i == numero:
        b = True
        print("Lo hallé") # output
if b == False:
    print("No lo hallé") # output