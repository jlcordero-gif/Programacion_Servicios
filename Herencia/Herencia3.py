class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular(self, cantidad):
        "Calcula el precio total según la cantidad"
        return self.precio * cantidad

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}"

    def __lt__(self, other):
        "Permite comparar productos por precio"
        return self.precio < other.precio


class Perecedero(Producto):
    def __init__(self, nombre, precio, dias_a_caducar):
        super().__init__(nombre, precio)
        self.dias_a_caducar = dias_a_caducar

    def calcular(self, cantidad):
        total = super().calcular(cantidad)
        if self.dias_a_caducar == 1:
            total /= 4
        elif self.dias_a_caducar == 2:
            total /= 3
        elif self.dias_a_caducar == 3:
            total /= 2
        return total

    def __str__(self):
        return f"Perecedero: {self.nombre}, Precio: {self.precio}, Días a caducar: {self.dias_a_caducar}"


class NoPerecedero(Producto):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo

    def __str__(self):
        return f"No perecedero: {self.nombre}, Precio: {self.precio}, Tipo: {self.tipo}"


# Ejemplos
if __name__ == "__main__":
    productos = [
        Producto("Agua", 1.0),
        Perecedero("Leche", 1.2, 1),
        Perecedero("Yogur", 2.0, 3),
        NoPerecedero("Arroz", 3.5, "Cereal"),
    ]

    for p in productos:
        print(p)
        print(f"Total por 5 unidades: {p.calcular(5)}\n")

    print("Es la leche es más barata que Arroz?", productos[1] < productos[3])
