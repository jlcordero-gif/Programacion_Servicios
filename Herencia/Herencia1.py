class Animal:
    def __init__(self, nombre, numeroPatas):
        self.nombre = nombre
        self.numeroPatas = numeroPatas

    def habla(self):
        pass

    def __str__(self):
        return f"Me llamo {self.nombre}, tengo {self.numeroPatas} patas y sueno asi: {self.habla()}"

class Gato(Animal):
    def __init__(self, nombre, numeroPatas=4):
        super().__init__(nombre, numeroPatas)

    def habla(self):
        return "Miau"
    
    def __str__(self):
        return super().__str__()

class Perro(Animal):
    def __init__(self, nombre, numeroPatas=4):
        super().__init__(nombre, numeroPatas)

    def habla(self):
        return "Guau"
    
    def __str__(self):
        return super().__str__()
    
#pruebas
if __name__ == "__main__":
    gato = Gato("Jenry")
    perro = Perro("Martin")

    print(gato)
    print(perro)
