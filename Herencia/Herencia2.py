class Empleado:
    def __init__(self, nombre=""):
        self.nombre = nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def __str__(self):
        return "Empleado " + self.nombre

class Operario(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        return super().__str__() + " -> Operario"

class Directivo(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        return super().__str__() + " -> Directivo"

class Oficial(Operario):
    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        return super().__str__() + " -> Oficial"

class Tecnico(Operario):
    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        return super().__str__() + " -> Tecnico"

if __name__ == "__main__":
    e1 = Empleado("Rafa")
    d1 = Directivo("Mario")
    o1 = Operario("Alfonso")
    of1 = Oficial("Luis")
    t1 = Tecnico("Pablo")

    print(e1)
    print(d1)
    print(o1)
    print(of1)
    print(t1)
