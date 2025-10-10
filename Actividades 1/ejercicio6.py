factorial = int(input("Introduce a factorial number: "))
contador = factorial

while contador > 1:
    contador = contador -1
    factorial *= contador 
    

print("The factorial of the introduced number is:", factorial)