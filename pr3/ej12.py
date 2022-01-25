def leer_entero_mayor_que(numero):
    n = int(input("Introduce un entero mayor que {}: ".format(numero)))
    while n <= numero:
       n = int(input("Esperaba entero mayor que {0} y {1} no lo es. Dame Otro: ".format(numero,n)))
    return n

def contar_divisores(i):
    div = 2
    if  i == 1:
        div = 1
        return div
    for n in range(2, i):
        if i % n == 0:
            div += 1
    return div

def es_primo(n):
    div = contar_divisores(n)
    if div > 2 or n == 1:
        return False
    else:
        return True

n = 0
algunPrimo = False
n = leer_entero_mayor_que(n)
a = leer_entero_mayor_que(n)

print("Voy a buscar primos entre {} y {}...".format(n,a))
print("Encontrados:", end=' ')
for i in range(n, a + 1):
    primo = es_primo(i)
    if(primo):
        algunPrimo = True
        print(i, end=' ')
if not algunPrimo:
    print("ninguno")