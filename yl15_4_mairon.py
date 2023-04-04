import random


punktid = 0


for i in range(10):
    x = random.randint(1,50)
    y = random.randint(1,50)
    print (x,"+",y,"=") 
    vastus = int(input())
    if vastus == x+y:
        print("Tubli!")
        punktid+=1
    else:
        print("VALE... Õige vastus on",x+y)
        

print("Said",punktid,"punkti")
