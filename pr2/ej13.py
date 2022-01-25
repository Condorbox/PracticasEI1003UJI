a = int(input("¿Cuántas veces prevés utilizar el gimnasio? "))

t = 50
b = a//10
c = a % 10
if c > 0:
    br = b + 1

bonos = br * 20
unidad = b * 20 + c * 3

final = min(t,bonos,unidad)

print("Con tarjeta: {0} euros.".format(t))
print("Con bonos ({0}): {1} euros.".format(br, bonos))
print("Con bonos ({0}) y entradas ({1}): {2} euros.".format(b, c, unidad))

if final == t:
    r = "tarjeta"
elif final == bonos:
    r = "bonos"
else:
    r = "bonos y entradas"

print("Recomendación: {0}.".format(r))