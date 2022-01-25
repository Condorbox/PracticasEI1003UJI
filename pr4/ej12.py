def leer_lista_enteros():
    numeros = []
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    n = input("Nuevo número: ")
    while n != '':
        n = int(n)
        numeros.append(n)
        n = input("Nuevo número: ")
    return numeros

def repetidos_lista(lista):
    newLista = []
    for i in range(len(lista)):
        if lista.count(lista[i]) > 1:
            newLista.append(lista[i])
    res = [i for n, i in enumerate(newLista) if i not in newLista[:n]]
    return res

def suma_lista(lista):
    suma = 0
    for i in range(len(lista)):
       suma += lista[i]
    return suma

n = leer_lista_enteros()
m = repetidos_lista(n)
suma = suma_lista(m)
print("Números leídos más de una vez (suman {0}): {1}".format(suma, m))
print("Todos los números leídos: {}".format(n))
