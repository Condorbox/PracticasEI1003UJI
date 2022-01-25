
def contar_divisores(i):
    div = 0
    for a in range(1, i + 1):
        if (i % a == 0):
            div += 1
    return div

divMax = 0
max = 0
n = int(input("Introduce un número entero: "))
for i in range(1, n + 1):
    div = contar_divisores(i)
    if (divMax <= div):
        divMax = div
        max = i
print("El número con más divisores es {} ({} divisores)".format(max, divMax))

