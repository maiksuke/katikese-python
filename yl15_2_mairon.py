a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

while a**2+b**2!=c**2:
    print("Ei teki kolmnurka")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))   

umbermoot = a+b+c
pindala = (a+b+c)/2

if a**2+b**2==c**2:
    print("Ümbermõõt on",umbermoot)
    print("Pindala on on",pindala)
