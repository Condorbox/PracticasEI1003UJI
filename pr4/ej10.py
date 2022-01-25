def leer_lista_enteros():
    numeros = []
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    n = input("Nuevo número: ")
    while n != '':
        n = int(n)
        numeros.append(n)
        n = input("Nuevo número: ")
    return numeros

def posición_menor(lista):
    min = lista[0]
    p = 0
    for i in range(len(lista)):
        if min > lista[i]:
            min = lista[i]
            p = i
    return p

def intercambiar(lista, i, j):
    newLista = lista[:]
    if i != j:
        lista[i] = newLista[j]
        lista[j] = newLista[i]

n = leer_lista_enteros()
print("Lista leída: {}".format(n))
if not n == []:
    p = posición_menor(n)
    intercambiar(n, p, 0)

print("Modificada: {}".format(n))