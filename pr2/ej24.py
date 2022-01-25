a = int(input("Introduce un número entero: "))

n = 1

for i in range(1, a//2 + 1):
    if a % i == 0:
        n += 1
print("El número {0} tiene {1} divisores".format(a, n))