from moduloimagen import leerImagen, mostrarImagen
import numpy as np

def reflejar_vertical(imagen):
    inversaMal = np.flip(imagen)
    inversaBien = []
    for i in range(len(inversaMal)):
        inversaBien.append(np.flip(inversaMal[i]))
    CopiarMatriz(inversaBien, imagen)

def CopiarMatriz(n, m):
    for i in range(len(n)):
        for j in range(len(n[0])):
            m[i][j] = n[i][j]

nombreFichero = input("Introduce el nombre de la imagen: ")
imagen = leerImagen(nombreFichero)
reflejar_vertical(imagen)
mostrarImagen(imagen)