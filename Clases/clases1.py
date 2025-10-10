class CuentaCorriente:
        def __init__(self, DNI, nombre="", saldo=0.0):
                self.DNI = DNI
                self.nombre = nombre
                self.saldo = saldo


        def get_DNI(self):
                return self.DNI

        def get_nombre(self):
                return self.nombre

        def get_saldo(self):
                return self.saldo

        def sacar_dinero(self, cantidad):
                if cantidad > self.saldo:
                        print("Saldo insuficiente.")
                else:
                        self.saldo -= cantidad
                        print(f"Has sacado {cantidad} euros, tu nuevo saldo es de {self.saldo} euros")

        def ingresar_dinero(self, cantidad):
                self.saldo += cantidad
                print(f"Has ingreasado {cantidad} euros, tu nuevo saldo es de {self.saldo} euros")

        def __str__(self):
                return "Tu cuenta: \n DNI" + self.DNI + "\n Nombre: " + self.nombre + "\n Saldo: " + str(self.saldo) + " euros"

        def __eq__ (self, otraCuenta):
                iguales = False
                if self.DNI == otraCuenta.DNI:
                        iguales = True
                return iguales

        def __lt__(self, otraCuenta):
                menor = False
                if self.saldo < otraCuenta.saldo:
                        menor = True
                if menor == True:
                        print(f"{self.nombre} tiene menos dinero que {otraCuenta.nombre}")
                return menor


#pruebas 
if __name__ == "__main__":
        # Crear instancias de la clase Libro
        Persona1 = CuentaCorriente("82390", "Gabriel García Márquez", 10)
        Persona2 = CuentaCorriente("82390", "Miguel de Cervantes", 5)

        # Mostrar información de las personas
        print(Persona1)
        print(Persona2)

        # Sacar dinero
        Persona1.sacar_dinero(5)

        # Ingresar dinero
        Persona2.ingresar_dinero(15)

        # Comparar personas
        print("¿Tienen la misma cuenta corriente?", Persona1 == Persona2)
        print("¿La persona 1 tiene menos dinero que la persona 2?", Persona1 < Persona2)
    
