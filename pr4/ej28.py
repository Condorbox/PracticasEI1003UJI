from moduloimagen import leerImagen, mostrarImagen

def nueva_matriz(filas, columnas, valor):
    matriz = []
    for i in range(filas):
        matriz.append([valor] * columnas)
    return matriz

def binarizada(imagen, umbral):
    filas = len(imagen)
    columnas = len(imagen[0])
    matriz = nueva_matriz(filas, columnas, umbral)
    for i in range(filas):
        for j in range(columnas):
            if imagen[i][j] <= umbral:
                matriz[i][j] = 0
            else:
                matriz[i][j] = 255
    return matriz


nombreFichero = input("Introduce el nombre de la imagen: ")
imagen = leerImagen(nombreFichero)
n = int(input("Introduce el umbral: "))
matriz = binarizada(imagen, n)
mostrarImagen(matriz)


