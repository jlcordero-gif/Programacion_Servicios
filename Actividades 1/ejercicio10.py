def main():
	a = int(input("Introduce el primer número entero: "))
	b = int(input("Introduce el segundo número entero: "))
	print("El máximo es ", maximo(a, b))
	
def maximo(a, b):
    if a > b:
        return a
    else:
        return b
    
main()
