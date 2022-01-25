while True:
    a = float(input("Introduce el lado a: "))
    b = float(input("Introduce el lado b: "))
    c = float(input("Introduce el lado c: "))

    if (a + b > c) and (a + c > b) and (b + c > a):
        break
    print("No es un triángulo")

if a != b and a != c and b != c:
    print("Es escaleno")
elif a == b and a == c and b == c:
    print("Es equilátero")
else:
    print("Es isósceles")
