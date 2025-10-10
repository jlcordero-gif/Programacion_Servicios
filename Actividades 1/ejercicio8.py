num = int(input(("Introduce a number: ")))

#Dibujar triangulo de base y altura num

for i in range(1, num + 1):
    print(" " * (num - i) + '* ' * i)