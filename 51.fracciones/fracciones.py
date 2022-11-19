# serie = 1/1, 1/2, 1/3, 1/4, 1/5,...
n = int(input("Número de elementos: "))
s = "Serie: "

for i in range(1, n+1):
    if i < n:
        s = s + "1/" + str(i) + ","
    else:
        s = s + "1/" + str(i)
print(s)
