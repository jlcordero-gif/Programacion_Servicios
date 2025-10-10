def esVocal(letra):
    if len(letra) == 1 and letra in "aeiouAEIOU":
        print("Es vocal")
    else:
        print("No es vocal")
    
letra = input("Es vocal?: ")
esVocal(letra)
