a = float(input("Introduce un número: "))
media = 0
minimo = a
maximo = a
i = 0

if a > 0:
    while a >= 0:
        i += 1
        media += a
        minimo = min(minimo, a)
        maximo = max(maximo, a)
        a = float(input("Introduce otro número: "))
    print("Media: {0}".format(media/i))
    print("Mínimo: {0}".format(minimo))
    print("Máximo: {0}".format(maximo))
else:
    print("No se han introducido datos")

