import math

a = float(input("Introduce el radio: "))

area = math.pi * a ** 2
long = math.pi * a * 2

print("Área: {0: 0.02f}".format(area))
print("Longitud: {0: 0.02f}".format(long))