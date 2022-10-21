# Ejercicio No. 29: Registro centinela.

# input
codigo = int(input("Ingrese el código del estudiante o digite 0 para terminar: "))
nota_parcial1 = float(input("Ingrese la nota del primer parcial: "))
nota_parcial2 = float(input("Ingrese la nota del segundo parcial: "))
nota_parcial3 = float(input("Ingrese la nota del tercer parcial: "))

# processing
cant_reprobados = 0

while codigo != 0:
    nota_final = (nota_parcial1 + nota_parcial2 + nota_parcial3)/ 3
    print("El estudiante de código", codigo, "obtuvo una nota final de", nota_final)

    if nota_final < 3:
        cant_reprobados += 1
    
    codigo = int(input("Ingrese el código del estudiante o digite 0 para terminar: "))
    nota_parcial1 = float(input("Ingrese la nota del primer parcial: "))
    nota_parcial2 = float(input("Ingrese la nota del segundo parcial: "))
    nota_parcial3 = float(input("Ingrese la nota del tercer parcial: "))

# output
print("Cantidad de reprobados:", cant_reprobados)