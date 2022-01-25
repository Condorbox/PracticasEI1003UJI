from modulomatrices import leerMatrizEnteros, mostrarMatriz

def sumar_encima_diagonal(matriz):
    suma = 0
    numFilas = len(matriz)
    numColumnas = len(matriz[0])
    if numColumnas != numFilas:
        return None
    for i in range(0, numFilas - 1):
        for j in range(i, numFilas - 1):
            suma += matriz[i][j + 1]
    return suma

nombreFichero = input("Introduce el nombre de un fichero: ")
matriz = leerMatrizEnteros(nombreFichero)
suma = sumar_encima_diagonal(matriz)

if suma == None:
    print("Error. Se requiere una matriz cuadrada")
else:
    print("La suma de los elementos por encima de la diagonal principal es {}".format(suma))