class Libro:
    def __init__(self, titulo, autor, ejemplares, ejemplaresVendidos=0):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares
        self.ejemplaresVendidos = ejemplaresVendidos

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_ejemplares(self):
        return self.ejemplares

    def get_ejemplaresVendidos(self):
        return self.ejemplaresVendidos

    def prestamo(self):
        if self.ejemplares > 0:
            self.ejemplares -= 1
            self.ejemplaresVendidos += 1
            print(f"Has prestado un ejemplar de {self.titulo}, quedan {self.ejemplares} ejemplares.")
            return True
        else:
            print("No hay ejemplares disponibles para préstamo.")
            return False

    def devolucion(self):
        if self.ejemplaresVendidos > 0:
            self.ejemplares += 1
            self.ejemplaresVendidos -= 1
            print(f"Has devuelto un ejemplar de {self.titulo}, quedan {self.ejemplares} ejemplares.")
            return True
        else:
            print("No puedes devolver nada")
            return False

    def __str__(self):
        return(f"Libro: {self.titulo} \n Autor: {self.autor} \n Ejemplares: {self.ejemplares} \n Ejemplares vendidos: {self.ejemplaresVendidos}")

    def __eq__(self, otroLibro):
        iguales = False
        if self.titulo == otroLibro.titulo and self.autor == otroLibro.autor:
            iguales = True
        return iguales

    def __lt__(self, otroLibro):
        menor = False
        if self.ejemplaresVendidos < otroLibro.ejemplaresVendidos:
            menor = True
        return menor


#pruebas 
if __name__ == "__main__":
    # Crear instancias de la clase Libro
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 10)
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 5)

    # Mostrar información de los libros
    print(libro1)
    print(libro2)

    # Realizar un préstamo
    libro1.prestamo()

    # Devolver un libro
    libro1.devolucion()

    # Comparar libros
    print("¿Son iguales los libros?", libro1 == libro2)
    print("¿El libro 1 tiene menos ejemplares vendidos que el libro 2?", libro1 < libro2)

