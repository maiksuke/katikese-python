import random


punktid = 0
tehete_arv = int(input("Mitu tehet soovite? "))
min_piir = int(input("Miinimum arvude piir: "))
max_piir = int(input("Maksimum arvude piir: "))

for i in range(tehete_arv):
    x = random.randint(min_piir,max_piir)
    y = random.randint(min_piir,max_piir)
    print (x,"+",y,"=") 
    vastus = int(input())
    if vastus == x+y:
        print("Tubli!")
        punktid+=1
    else:
        print("VALE... Õige vastus on",x+y)
        

print("Said",punktid,"punkti")

if punktid >= .9*tehete_arv:
    print("Ülihea! Said",punktid,"punkti.")
elif punktid >= .75*tehete_arv:
    print("Olid tubli! Said",punktid,"punkti.")
elif punktid >= .50*tehete_arv:
    print("Korralik keskmine tulemus! Said",punktid,"punkti.")
elif punktid >= .25*tehete_arv:
    print("Püüad järgmisel korral rohkem. Said",punktid,"punkti.")
else: print(":( Said",punktid,"punkti.")