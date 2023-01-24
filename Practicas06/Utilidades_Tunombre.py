# Programa que dada cuatro funciones introduce un nombre en una matriz

class Empleado:
    def __init__(self):
        self.nombre = input("Introduce el nombre del empleado")
        self.sueldo = float(input("Introduce el sueldo de empleado"))

    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Sueldo: ", self.sueldo)
    def paga_impuestos(self):
        if(self.sueldo > 3000):
            print("Debe pagar impuestos")
        else:print("No debe pagar impuestos")

empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
print(type(empleado1))
