def main():
	a = int(input("Introduce el primer número entero: "))
	b = int(input("Introduce el segundo número entero: "))
	print("Números entre {a} y {b}:")
	entre(a, b)

def entre(a, b):
	if a < b:
		for i in range(a + 1, b):
			print(i)
	elif a > b:
		for i in range(b + 1, a):
			print(i)
	else:
		print("No hay números entre los valores dados.")
		
main()