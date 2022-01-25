
str = input("Introduce una cadena de caracteres: ")
esNum = True
posicion = 0
suma = 0

for i in range(0, len(str)):
    if not str[i].isnumeric():
        esNum = False
        posicion = i
        break

def SumaCadena():
    suma = 0
    for i in range(0, len(str)):
        suma += int(str[i])
    return suma

if esNum:
    print("Todos los caracteres son dígitos")
    print("¿Cuántos dígitos? {}".format(len(str)))
    suma = SumaCadena()
    print("¿Suma de dígitos? {}".format(suma))
else:
    print('Primer "no dígito": ' + "'{}' en posición {}".format(str[posicion], posicion))