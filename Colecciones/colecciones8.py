d = { 
    "Salsa de llave acida": 32,
    "Salsa de lotus": 10,
    "Chocolate dubai": 101,
}

def añadir_venta(producto, cantidad):
    if producto in d:
        d[producto] += cantidad
    else:
        d[producto] = cantidad
    print(f"Se ha añadido {cantidad} ventas de {producto}.")

def calcular_ventas(producto):
    if producto in d:
        print(f"El total de ventas de {producto} es {d[producto]}.")
    else:
        print("El producto no existe.")

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Añadir venta")
    print("2. Calcular ventas")
    print("3. Salir")

mostrar_menu()

opcion = input("Selecciona una opción (1-3): ")
while opcion != '3':
    if opcion == '1':
        producto = input("Introduce el nombre del producto: ")
        cantidad = int(input("Introduce la cantidad vendida: "))
        añadir_venta(producto, cantidad)
    elif opcion == '2':
        producto = input("Introduce el nombre del producto que quieras ver: ")
        calcular_ventas(producto)
    else:
        print("Opcion no valida")
    
    mostrar_menu()
    opcion = input("Selecciona una opción (1-3): ")
    