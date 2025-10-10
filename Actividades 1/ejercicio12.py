def calculadora():
    a = int(input("Introduce el primer número real: "))
    b = int(input("Introduce el segundo número real: "))

    operacion = input("Introduce la operación (+, -, *, /): ")

    if operacion == "+":
        print(f"{a} + {b} = {a + b}")
    elif operacion == "-":
        print(f"{a} - {b} = {a - b}")
    elif operacion == "*":
        print(f"{a} * {b} = {a * b}")
    elif operacion == "/":
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("Error: División por cero")


calculadora()