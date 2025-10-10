num = int(input("Introduce a full positive number: "))
primo = False
for contador in range (2, num + 1, 1):
    uno = num / contador
    prueba = num % contador
    if prueba != 0 and uno == primo:
        primo = True   
    else:
        print("The number isn't prime")
        exit()
        
if primo == True:
    print("The number is prime")

    