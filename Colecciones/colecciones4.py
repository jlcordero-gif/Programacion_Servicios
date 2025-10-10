lista = input("Dame 10 numeros separados por comas: ").split(",")

numeros = [int(numero) for numero in lista]
print(numeros)

ordenados = sorted(numeros)
print("Números ordenados de menor a mayor: ", ordenados)