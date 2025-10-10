d = { 
    "ChiquiIbai": "123456789",
    "Xxtentacion": "987654321",
    "Milo J": "456789123"
}

def agregar_contacto(nombre, telefono):
    if nombre in d:
        print("El contacto ya existe.")
    else:
        d[nombre] = telefono
        print(f"Contacto {nombre} agregado")

def eliminar_contacto(nombre):
    if nombre in d:
        del d[nombre]
        print(f"Contacto {nombre} eliminado")
    else:
        print("El contacto no existe.")

def buscar_contacto(nombre):
    if nombre in d:
        print(f"El número de {nombre} es {d[nombre]}.")
    else:
        print("El contacto no existe.")

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Salir")

mostrar_menu()
opcion = input("Selecciona una opción (1-4): ")

while opcion != '4':
    if opcion == '1':
        nombre = input("Introduce el nombre del contacto: ")
        telefono = input("Introduce el número de teléfono: ")
        agregar_contacto(nombre, telefono)
    elif opcion == '2':
        nombre = input("Introduce el nombre del contacto a eliminar: ")
        eliminar_contacto(nombre)
    elif opcion == '3':
        nombre = input("Introduce el nombre del contacto a buscar: ")
        buscar_contacto(nombre)
    else:
        print("Opcion no valida")
    
    opcion = input("Selecciona una opción (1-4): ")
    mostrar_menu()
   