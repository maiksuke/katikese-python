import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))


def ruutvorrand(a, b, c):
    diskriminant = b ** 2 - 4 * a * c

    vastuseruut = math.sqrt(abs(diskriminant))

    if diskriminant > 0:
        print("x1 on",(-b + vastuseruut)/(2 * a))
        print("x2 on",(-b - vastuseruut)/(2 * a))

    elif diskriminant == 0:
        print(-b / (2 * a))

    else: print("Lahendid puuduvad.")

if a == 0:
    print("Sisesta õige ruutvõrrand")
else:ruutvorrand(a, b, c)

