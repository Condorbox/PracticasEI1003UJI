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

n = int(input("Introduce un número entero: "))
print("Los números abundantes menores que {} son: ".format(n), end=' ')
for i in range (1, n):
    abundante = es_abundante(i)
    if abundante:
     print(i, end=' ')