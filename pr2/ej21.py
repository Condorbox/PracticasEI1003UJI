n = int(input("Introduce un número entero: "))

i = 1
for i in range(1, n):
    a = i**2
    if(a > n - 1):
        break
    print("El cuadrado de {0} es {1}".format(i, a))