
n = input("Introduce un texto (vacío para acabar): ")
min = n
max = n

while n != '':
    n = input("Introduce otro texto (vacío para acabar): ")
    if len(n) >= len(max):
        max = n
    if len(n) <= len(min) and n != '':
        min = n

if min == '':
    print("No se ha introducido ningún texto")
else:
    print("Última cadena de mínima longitud, {}: =>{}<=".format(len(min), min))
    print("Última cadena de máxima longitud, {}: =>{}<=".format(len(max), max))
