class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    #getters
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    #string
    def __str__ (self):
        return f"({self.x}, {self.y})"
    
    #setter
    def setXY(self, x, y):
        self.x = x
        self.y = y

    #otros metodos
    def desplazar(self, dx, dy):
        self.x += dx
        self.y += dy

    def distancia(self, otroPunto):
        return ((self.x - otroPunto.x)**2 + (self.y - otroPunto.y)**2)**0.5
    
#pruebas
if __name__ == "__main__":
    p1 = Punto(3, 4)
    p2 = Punto(1, 2)

    print("Punto 1:", p1)
    print("Punto 2:", p2)



    print("Distancia entre p1 y p2:", p1.distancia(p2))

    p1.desplazar(1, -1)
    print("Punto 1 después de desplazar:", p1)

    print("Nueva distancia entre p1 y p2:", p1.distancia(p2))
