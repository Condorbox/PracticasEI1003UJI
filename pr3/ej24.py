def strLen(str):
    len = 0
    for i in str:
        len += 1
    return len

def Sufijo(a, b):
    lenB = strLen(b)
    for i in range(-1, -lenB - 1, -1):
        if not b[i] == a[i]:
            return False
    return True

a = input("Introduce una cadena de caracteres A: ")
b = input("Introduce una cadena de caracteres B: ")

lenA = strLen(a)
lenB = strLen(b)

if lenB > lenA:
    print("B no es sufijo de A")
else:
    sufijo = Sufijo(a, b)
    if sufijo or b == '':
        print("B es sufijo de A")
    else:
        print("B no es sufijo de A")
