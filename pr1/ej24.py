import math

a = float(input("Introduce el primer lado: "))
b = float(input("Introduce el segundo lado: "))
c = float(input("Introduce el ángulo (en grados): "))

c = c*math.pi/180
area = (a*b/2)*math.sin(c)

print("El área del triángulo es: {0:0.02f}".format(area))