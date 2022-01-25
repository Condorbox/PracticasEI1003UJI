
def contar_secuencias_dígitos(str):
    secuencias = 0
    primerNumerico = False
    for i in range(0, len(str)):
        if str[i].isnumeric():
            if not primerNumerico:
                secuencias = 1
            primerNumerico = True
        if not str[i].isnumeric() and i + 1 < len(str) and str[i + 1].isnumeric() and primerNumerico:
            secuencias += 1
    return secuencias

print("Ve introduciendo cadenas de caracteres, o vacío para acabar...")
str = input("Nueva cadena: ")

while str != '':
    secuencias = contar_secuencias_dígitos(str)
    print("Secuencias de dígitos encontradas: {}".format(secuencias))
    str = input("Nueva cadena: ")

print("¡Adiós!")