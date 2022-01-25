def LeerLista():
    lista = []
    print("Ve introduciendo candidaturas, o vacío para acabar...")
    n = input("Nueva candidatura: ")
    while n != '':
        lista.append(n)
        n = input("Nueva candidatura: ")
    return lista

def NumerosDeVostos(candidaturas):
    votos = []
    for i in range(len(candidaturas)):
        n = int(input("Votos para {}: ".format(candidaturas[i])))
        votos.append(n)
    return votos

def CalculoDeVotos(candidaturas, votos):
    total = Suma(votos)
    for i in range(len(candidaturas)):
        porcentaje = (votos[i]/total)*100
        print("{0:.2f}% de los votos a candidaturas para {1}".format(porcentaje, candidaturas[i]))

def Suma(lista):
    suma = 0
    for i in range(len(lista)):
       suma += lista[i]
    return suma

n = LeerLista()
m = NumerosDeVostos(n)
CalculoDeVotos(n, m)