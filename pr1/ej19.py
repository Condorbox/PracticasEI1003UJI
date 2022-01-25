a = (input("Introduce una cadena: "))
b = (input("Introduce un separador: "))
c = int(input("Introduce un número entero: "))
i = 0
x = ""

while i < c - 1:
    x += a + b
    i += 1


print("{0}".format(x + a))