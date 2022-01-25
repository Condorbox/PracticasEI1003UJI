
def tipo_triángulo(a, b, c):
    esTriangulo = es_triángulo(a, b, c)
    if(esTriangulo):
        if a != b and a != c and b != c:
            str = "escaleno"
            return str
        elif a == b and a == c and b == c:
            str = "equilátero"
            return str
        else:
            str = "isósceles"
            return  str
    else:
        return None

def es_triángulo(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return  True
    else:
        return False


while True:
    a = float(input("Introduce el lado a: "))
    b = float(input("Introduce el lado b: "))
    c = float(input("Introduce el lado c: "))

    if (es_triángulo(a, b, c)):
        print("es {0}".format(tipo_triángulo(a, b, c)))
        break
    else:
        print("No es un triángulo")




