import math

tope = int(input("Introduce un número entero: "))

print('Los {0} primeros números primos son:'.format(tope), end=' ')

n = 1
c = 0

while c < tope:
    esPrimo = True
    n += 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            esPrimo = False
            break
    if esPrimo:
        c += 1
        print(n, end=' ')
