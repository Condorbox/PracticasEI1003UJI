import math

a = float(input("Introduce a: "))
b = float(input("Introduce b: "))
c = float(input("Introduce c: "))

print("x1 = {0}".format((-b + math.sqrt((b**2 - 4*a*c)))/(2*a)))
print("x2 = {0}".format((-b - math.sqrt((b**2 - 4*a*c)))/(2*a)))