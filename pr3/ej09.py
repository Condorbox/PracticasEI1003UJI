def sumar_divisores_propios(n):
    num = 0
    for i in range(1, n):
        if n%i == 0:
            num += i
    return num

def es_abundante(n):
    num = sumar_divisores_propios(n)
    if n < num:
        return True
    else:
        return False
i = 0
iteraciones = 0
n = int(input("Introduce un número entero: "))
print("Los {} primeros números abundantes son: ".format(n), end=' ')
while True:
    abundante = es_abundante(i)
    if abundante:
        iteraciones += 1
        print(i, end=' ')
    if iteraciones == n:
        break
    i += 1