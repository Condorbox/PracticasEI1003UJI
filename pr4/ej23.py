from modulomatrices import leerMatrizEnteros, mostrarMatriz

def producto_diagonal_secundaria(matriz):
    producto = 1
    numFilas = len(matriz)
    numColumnas = len(matriz[0])
    if numColumnas != numFilas:
        return None
    for i in range(0, numFilas):
        producto *= matriz[i][(numColumnas - 1) - i]
    return producto

nombreFichero = input("Introduce el nombre de un fichero: ")
matriz = leerMatrizEnteros(nombreFichero)
producto = producto_diagonal_secundaria(matriz)

if producto == None:
    print("Error. Se requiere una matriz cuadrada")
else:
    print("El producto de los elementos en la diagonal secundaria es {}".format(producto))
