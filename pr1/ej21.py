import math

a = float(input("Introduce el radio: "))

def área_círculo(radio):
    return math.pi * radio ** 2

x = área_círculo(a)

print("Área: {0}".format(x))
