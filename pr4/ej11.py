def leer_lista_enteros():
    numeros = []
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    n = input("Nuevo número: ")
    while n != '':
        n = int(n)
        numeros.append(n)
        n = input("Nuevo número: ")
    return numeros

def posición_menor(lista, offset):
    min = lista[offset]
    p = offset
    for i in range(offset, len(lista)):
        if min > lista[i]:
            min = lista[i]
            p = i
    return p

def intercambiar(lista, i, j):
    newLista = lista[:]
    if i != j:
        lista[i] = newLista[j]
        lista[j] = newLista[i]

def ordenar_lista(lista):
    for i in range(len(lista)):
        menor = posición_menor(lista, i)
        intercambiar(lista, menor, i)

n = leer_lista_enteros()
print("Lista leída: {}".format(n))
if n != []:
    ordenar_lista(n)
print("Lista ordenada: {}".format(n))