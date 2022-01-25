import math

tope = int(input("Introduce un número entero: "))

print('Los números primos menores que {0} son:'.format(tope), end=' ')
for n in range(2, tope):
    es_primo = True
    for candidato in range(2, int(math.sqrt(n)) + 1):
        if n % candidato == 0:
            es_primo = False
            break
    if es_primo:
        print(n, end=' ')