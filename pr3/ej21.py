
def es_letra_castellana(caracter):
    otrasLetras = "ñáéíóúü"
    if caracter>='a' and caracter<= 'z' or caracter in otrasLetras:
        return True
    else:
        return False

def primer_no_castellana(str):
    isLetra = True
    for i in range(0, len(str)):
        isLetra = es_letra_castellana(str[i])
        if not isLetra:
            return str[i]

print("Ve introduciendo palabras, o vacío para acabar...")
str = input("Nueva palabra: ")
while str != "":
    str = str.lower()
    isLetra = primer_no_castellana(str)

    if isLetra == None:
        print("Podría ser una palabra correcta")
    else:
        print("Contiene un carácter que no es del alfabeto castellano: '{}'".format(isLetra))

    str = input("Nueva palabra: ")

print("¡Adiós!")
