# serie = 1, 4, 9, 16, 25, 36, 49...
n = int(input("Número de elementos: "))
s = "Serie: "
for i in range(1, n+1):
    if i < n:
        s = s + str(i**2) + ","
    else:
        s = s + str(i**2)
print(s)
