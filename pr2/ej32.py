import math


n = int(input("Introduce un número entero: "))

for i in range(1, n + 1):
    for a in range(1, i + 1):
        factorial = math.factorial(a)
    print("{0}! = {1}".format(i, factorial))