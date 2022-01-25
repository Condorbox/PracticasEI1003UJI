
def evaluación_test(correctas, respuestas):
    if len(respuestas) != len(correctas):
        return None
    bien = 0
    mal = 0
    for i in range(len(respuestas)):
        if respuestas[i] == correctas[i]:
            bien += 1
        elif respuestas[i].isalpha():
            mal += 1
    return [bien, mal, len(respuestas) - (bien + mal)]

respCorrectas = input("Introduce la plantilla de respuestas correctas: ")
print("Ve introduciendo respuestas de alumnos, o vacío para acabar...")
respuestas = input("Nuevas respuestas: ")

nAlumnos = 0

while respuestas != '':
    resultados = evaluación_test(respCorrectas, respuestas)
    if resultados == None:
        print("La cadena introducida es de longitud {0} (se esperaba {1})".format(len(respuestas), len(respCorrectas)))
    else:
        print("Resultados: {0} Bien; {1} Mal; {2} NS/NC".format(resultados[0], resultados[1], resultados[2]))
        nAlumnos += 1
    respuestas = input("Nuevas respuestas: ")

print("Alumnos corregidos: {}".format(nAlumnos))