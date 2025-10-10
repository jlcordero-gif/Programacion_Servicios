lista = input("Dame 10 numeros separados por comas: ").split(",")


numeros = [int(numero) for numero in lista]
print(numeros)

print("El máximo es: ", max(numeros))
print("El mínimo es: ", min(numeros))