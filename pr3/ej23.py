
def Respuestas(correctas):
    while True:
        respuesta = input("Nuevas respuestas: ")
        if len(respuesta) == len(correctas) or respuesta == '':
            break
        print("La cadena introducida es de longitud {} (se esperaba {})".format(len(respuesta), len(correctas)))
    return respuesta

def Correcciones(respuestas, correctas):
    bien = 0
    mal = 0
    for i in range(0, len(respuestas)):
        if respuestas[i] == correctas[i]:
            bien += 1
        elif respuestas[i].isalpha():
            mal += 1
    print("Resultados: {} BIEN; {} MAL; {} NS/NC".format(bien, mal, len(respuestas) - (bien + mal)))

respCorrectas = input("Introduce la plantilla de respuestas correctas: ")
print("Ve introduciendo respuestas de alumnos, o vacío para acabar...")
respuestas = Respuestas(respCorrectas)
nAlumnos = 0
while respuestas != '':
    Correcciones(respuestas, respCorrectas)
    nAlumnos += 1
    respuestas = Respuestas(respCorrectas)

print("Alumnos corregidos: {}".format(nAlumnos))

