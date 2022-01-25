def leer_lista_enteros():
    numeros = []
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    n = input("Nuevo número: ")
    while n != '':
        n = int(n)
        numeros.append(n)
        n = input("Nuevo número: ")
    return numeros

def borrar_elemento(lista, posicion):
    if posicion >= 0 and posicion <= len(lista) - 1:
       lista.pop(posicion)
       return  True
    else:
        return False

n = leer_lista_enteros()

while n != []:
    p = int(input("¿Qué posición debo eliminar de {}? ".format(n)))
    b = borrar_elemento(n, p)
    if not b:
        print("Posición incorrecta")

print("La lista ha quedado vacía")