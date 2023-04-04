nimi = input("Eesnimi: ")
perekonnanimi = input("Perekonnanimi: ")
if len(nimi) < len(perekonnanimi):
    print("Perekonnanimi on pikem")
elif len(nimi) > len(perekonnanimi):
        print("Eesnimi on pikem")
elif len(nimi) == len(perekonnanimi):
        print("Eesnimi ja perekonnanimi on sama pikkusega")

