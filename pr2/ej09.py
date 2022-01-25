import math

a = float(input("Introduce el lado a: "))
b = float(input("Introduce el lado b: "))
c = float(input("Introduce el lado c: "))

if (math.sqrt(a**2 + b**2) == c) or (math.sqrt(a**2 + c**2) == b) or (math.sqrt(c**2 + b**2) == a):
    print("Es rectángulo")
else:
    print("No es rectángulo")