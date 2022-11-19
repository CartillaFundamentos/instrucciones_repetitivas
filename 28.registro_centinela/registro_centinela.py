# Ejercicio No. 28: Registro centinela.

# input
codigo = int(input("Ingrese un código de estudiante o 0 para terminar: "))

# processing
reprobados = 0

while codigo != 0:
    parcial1 = float(input("Ingrese la nota del primer parcial: "))
    parcial2 = float(input("Ingrese la nota del segundo parcial: "))
    parcial3 = float(input("Ingrese la nota del tercer parcial: "))

    nota_final = (parcial1 + parcial2 + parcial3)/ 3
    print("El estudiante de código", codigo, "obtuvo una nota final de", nota_final)

    if nota_final < 3:
        reprobados += 1
    
    codigo = int(input("Ingrese un código de estudiante o 0 para terminar: "))

# output
print("Cantidad de reprobados:", reprobados)