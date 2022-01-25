def leer_alturas():
    numeros = []
    i = 0
    print("Ve introduciendo alturas sobre el nivel del mar, o una cadena vacía para acabar...")
    n = input("Altura en metros en el punto kilométrico {}: ".format(i))
    while n != '':
        n = int(n)
        numeros.append(n)
        i += 1
        n = input("Altura en metros en el punto kilométrico {}: ".format(i))
    return numeros

def mostrar_tramos_subida(alturas):
    comienzo = 0
    longitud = 0
    for i in range(1, len(alturas)):
        if alturas[i] > alturas[i-1]:
            longitud += 1
        else:
            print(comienzo, longitud)
            longitud = 0
            comienzo = i

def mostrar_tramos(tramo,inicio, longitud, desnivel):
    print(tramo, inicio, longitud, desnivel)

n = leer_alturas()
mostrar_tramos_subida(n)