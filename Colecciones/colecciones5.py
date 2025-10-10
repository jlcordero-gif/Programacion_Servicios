import random

contenedor = [random.randint(1, 10) for _ in range(100)]

N = int(input("¿Qué valor quieres buscar (entre 1 y 10)? "))

cantidad = contenedor.count(N)

print(f"El valor {N} aparece {cantidad} veces en la lista.")

