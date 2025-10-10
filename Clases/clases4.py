class Articulo:
    def __init__ (self, nombre, precio, IVA, cuantosQuedan):
        self.nombre = nombre
        self.precio = precio
        self.IVA = 21
        self.cuantosQuedan = cuantosQuedan

    def get_nombre(self):
        return self.nombre
    
    def get_precio(self):
        return self.precio  
    
    def get_cuantosQuedan(self):
        return self.cuantosQuedan
    
    def getPVP(self):
        return self.precio * (1 + self.IVA / 100)
    
    def getPVPDescuento(self, descuento):
        return self.getPVP() * (1 - descuento / 100)

    def vender(self, cantidad):
        if cantidad <= self.cuantosQuedan:
            self.cuantosQuedan -= cantidad
            print(f"Has vendido {cantidad} unidades de {self.nombre}, quedan {self.cuantosQuedan} unidades")
            return True
        else:
            print("No hay suficientes unidades para vender")
            return False
        
    def almacenar(self, cantidad):
        self.cuantosQuedan += cantidad
        print(f"Has almacenado {cantidad} unidades de {self.nombre}, ahora hay {self.cuantosQuedan} unidades")

    def __str__(self):
        return f"Articulo: {self.nombre} \n Precio sin IVA: {self.precio} \n IVA: {self.IVA}% \n Unidades en stock: {self.cuantosQuedan}"
    
    def __eq__(self, otroArticulo):
        iguales = False
        if self.nombre == otroArticulo.nombre:
            iguales = True
        return iguales
    
    def __lt__(self, otroArticulo):
        menor = False
        if self.nombre < otroArticulo.nombre:
            menor = True
        return menor
    

#pruebas
if __name__ == "__main__":
    articulo1 = Articulo("Salsa de lotus" , 3.5, 21, 10)
    articulo2 = Articulo("Salsa de llave acida" , 2.5, 21, 5)

    print(articulo1)
    print(articulo2)

    print("PVP del articulo 1:", articulo1.getPVP())
    print("PVP del articulo 2 con 10% de descuento:", articulo2.getPVPDescuento(10))

    articulo1.vender(3)
    articulo2.almacenar(10)

    print("Son el mismo articulo?", articulo1 == articulo2)
    print("El articulo 1 es menor que el articulo 2?", articulo1 < articulo2)


