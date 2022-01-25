from moduloimagen import leerImagen, mostrarImagen
import numpy as np

def reflejar_horizontal(imagen):
    inversa = []
    for i in range(len(imagen)):
        inversa.append(np.flip(imagen[i]))
    CopiarMatriz(inversa, imagen)

def CopiarMatriz(n, m):
    for i in range(len(n)):
        for j in range(len(n[0])):
            m[i][j] = n[i][j]

nombreFichero = input("Introduce el nombre de la imagen: ")
imagen = leerImagen(nombreFichero)
reflejar_horizontal(imagen)
mostrarImagen(imagen)


