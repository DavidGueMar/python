# Programa que simula el comportamiento de un almacén

class Almacen(object):
    def __init__(self,nombre="Murcia"):
        self.Nombre=nombre
        self.productosBBDD = {}
        self.__stock_minimo = 0

    def __setStock(self, valor, productos ):
        if valor <0:
            self.__stock_minimo =0
            return self.__stock_minimo
            print("Advertencia: productos por debajo del stock minimo: " + productos)
        elif valor>10:
            self.__stock_minimo = 10
            return self.__stock_minimo

    def __getStock(self):
        return self.__stock_minimo

    minimo = property(__setStock,__setStock)

    def ComprarProducto(self,nombre,categoria,cantidad):
        self.productos={}
        self.productos["nombre"]=nombre
        self.productos["categoria"]=categoria
        self.productos["cantidad"]=cantidad
        self.productosBBDD.append(self.productos)

    def VenderProducto(self,nombrePedir,categoriaPedir,cantidadPedir):
        if self.productos["nombre"]>cantidadPedir:
            self.productos["cantidad"] -= cantidadPedir
            return "vendido"
        else:
            print("No existe el producto en nuestro almacen o "
                  "la cantidad actual de nuestro almacen es " +self.productos["cantidad"])

        while categoriaPedir==self.productos["categoria"]:
            for self.productos["catgoria"] in self.productosBBDD:
                if self.productos["categoria"]> cantidadPedir:
                    print("Te recomendamos el producto "+self.productos["nombre"])

almacen1 = Almacen()

opcion=int(input("Teclee la opción \n "
                 "1.-Comprar producto \n "
                 "2.- Vender Producto \n "
                 "3 Mostrar productos \n "
                 "4 Actualizar stock minimo \n "
                 "0.-Salir \n "))
while opcion!=0:
    if opcion==1:
        almacen1.ComprarProducto("muñeca","juguetes",3)
    elif opcion==2:
        almacen1.VenderProducto("muñeca","juguetes",2)
    elif opcion ==3:
        pass
    elif opcion ==4:
        pass
    opcion = int(input("Teclee la opción \n "
                       "1.-Comprar producto \n "
                       "2.- Vender Producto \n "
                       "3 Mostrar productos \n "
                       "4 Actualizar stock minimo \n "
                       "0.-Salir \n "))