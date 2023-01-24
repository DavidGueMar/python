# Programa que emula el comportamiento de un ordenador

class Avion():

    def __init__(self, nombre, nAsientos=12):
        self.Nombre = nombre
        self.Nasientos = nAsientos
        self.Pasajeros = {}
        self.lNombre = ["juan", "paco", "pepe"]

        for i in range(0, nAsientos):
            self.Pasajeros["A - " + str(i)] = ["vacío"]
        print(self.Pasajeros.items())

    def asientos_libres(self):
        mensaje = ' '
        contador = 0

        for key in self.Pasajeros:
            mensaje += '[ El asiento: ' + key
            for pasajeros in self.Pasajeros[key]:
                 mensaje += ' se encuentra ' + str(pasajeros) + " ]"
                 if "vacio" in pasajeros:
                         contador +=1
        return mensaje

    def Comprar_billetes(self, nBilletes, *lNombre):
        lNombre=["juan","paco","pepe"]
        if self.asientos_libres() < int(nBilletes):
            print("No hay billetes suficientes")
        else:
            if "vacio" in self.Pasajeros.values():
                print("hay asientos vacios")



    def __str__(self):

        mensaje = ''

        for key in self.Pasajeros:
            mensaje +=  key +" : "
            for pasajeros in self.Pasajeros[key]:
                 mensaje += ' ' + str(pasajeros) +"\t"

        return mensaje

    def devolver_billete(self, nombre):
        if nombre in self.lNombre:
            self.lNombre.append("vacio")
        print(self.lNombre)




avion = Avion("paco", 4)
print(avion)

opcion = int(input("Introduce el número con la opción deseada: \n"
                   "\n1- Asientos libres: "
                   "\n2- Comprar Billetes: "
                   "\n3- Devolver Billetes: "
                   "\n4- Mostrar Avion: "
                   "\n5- Salir: \n"))
while (opcion != 0):
    if (opcion == 1):  # asientos libres
        print(avion.asientos_libres())
    elif (opcion == 2):  # comprar billetes
        # nombre= input("introduce el nombre ")
        avion.Comprar_billetes(2, "juan", "pepe")
    elif (opcion == 3):  # devolver billetes
        nombre =input("Introduce el nombre del billete a devolver")
        avion.devolver_billete(nombre)
    elif (opcion == 4):  # Mostrar avion
        print(avion)
    elif (opcion == 5):  # Salir
        break
    opcion = int(input("Introduce el número con la opción deseada: \n"
                       "\n1- Asientos libres: "
                       "\n2- Comprar Billetes: "
                       "\n3- Devolver Billetes: "
                       "\n4- Mostrar Avion: "
                       "\n5- Salir: \n"))
