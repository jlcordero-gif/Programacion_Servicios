import random

#crear numero random 
secretnum = random.randint(1, 100)

#prueba
"""print(secretnum)"""

#pedir numero
num = int(input("Introduce a number between 1 and 100 to try to find the secret number, to surrender, introuduce -1: "))

#condiciones
while 1 <= num <= 100:
    if num == secretnum:
        print("You got it!!!")
        exit()
    if num < secretnum:
        print("The secret number is higher")
        num = int(input("Try another time: "))
    if num > secretnum:
        print("The secret number is lower")
        num = int(input("Try another time: "))
    if num == -1:
        print("You lose")
        exit()

