lista = input("Dame 8 numeros separados por comas: ").split(",")


numeros = [int(numero) for numero in lista]
print(numeros)

for numero in numeros:
    if numero % 2 == 0:
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")

