
def leer_lista_enteros():
    numeros = []
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    n = input("Nuevo número: ")
    while n != '':
        n = int(n)
        numeros.append(n)
        n = input("Nuevo número: ")
    return numeros


def Cuadrados(lista):
    lista = numeros[:]
    for i in range(len(lista)):
        lista[i] = lista[i] ** 2
    return lista

numeros = leer_lista_enteros()
cuadrados = Cuadrados(numeros)

print("Cuadrados de los números leídos: {}".format(cuadrados))
print("Números leídos: {}".format(numeros))