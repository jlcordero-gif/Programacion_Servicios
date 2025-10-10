num = int(input(("Introduce positive numbers, to stop, introduce a negative number: ")))
suma = 0

#condicion 
while num >= 0:
    suma = int(suma) + num
    num = int(input("Another number: "))
else:
    print("The final sum is: ", str(suma))
