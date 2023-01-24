# Programa que simula el trabajo con ordenadores

class COrdenador(object):
    def __init__(self, CMarca, CProcesador, CPeso, CEstado, CPantalla):
        self.CMarca = CMarca
        self.CProcesador = CProcesador
        self.CPeso = CPeso
        self.CEstado = CEstado
        self.CPantalla = CPantalla

    def encenderOrdenador(self):
        if (self.CEstado == 'apagado'):
            self.CEstado = 'encendido'
            self.CPantalla = 'activa'
            print("Ordenador " + self.CEstado + "\n" + "Pantalla " + self.CPantalla)
        else:
            print("El ordenador ya está encendido")

    def apagarOrdenador(self):
        if (self.CEstado == 'encendido'):
            print("Apagando...")
            self.CEstado = 'apagado'
            self.CPantalla = 'inactiva'
            print("Ordenador " + self.CEstado + "\n" + "Pantalla " + self.CPantalla)
        else:
            print("El ordenador ya está apagado")

    def desactivarPantalla(self):
        if (self.CPantalla == 'activa'):
            print("Desactivando pantalla...")
            self.CPantalla = 'inactiva'
            print("Pantalla " + self.CPantalla)
        else:
            print("La pantalla ya está desactivada")

    def activarPantalla(self):
        if (self.CPantalla == 'inactiva'):
            print("Activando pantalla...")
            self.CPantalla = 'activa'
            print("Pantalla " + self.CPantalla)
        else:
            print("La pantalla ya está activada")

    def estadoDelOrdenador(self):
        print("Marca: " + str(self.CMarca) + "\n" +
              "Procesador: " + str(self.CProcesador) + "\n" +
              "Peso: " + str(self.CPeso) + "Kg" + "\n" +
              "El ordenador está " + str(self.CEstado) + "\n" +
              "La pantalla está " + str(self.CPantalla))

    def menu(self):
        miOrdenador = COrdenador('toshiba', 'amd', 3, 'apagado', 'inactiva')
        opcion = int(input("1=>Encender ordenador"
                           "\n2=>Apagar ordenador "
                           "\n3=>Desactivar pantalla "
                           "\n4=>Activar pantalla "
                           "\n5=>Estado"))
        while opcion != '':
            if opcion == 1:
                print("--------------------------------")
                miOrdenador.encenderOrdenador()
                print("--------------------------------")
            if opcion == 2:
                print("--------------------------------")
                miOrdenador.apagarOrdenador()
                print("--------------------------------")
            if opcion == 3:
                print("--------------------------------")
                miOrdenador.desactivarPantalla()
                print("--------------------------------")
            if opcion == 4:
                print("--------------------------------")
                miOrdenador.activarPantalla()
                print("--------------------------------")
            if opcion == 5:
                print("--------------------------------")
                miOrdenador.estadoDelOrdenador()
                print("--------------------------------")
            opcion = int(input("1=>Encender ordenador"
                               "\n2=>Apagar ordenador "
                               "\n3=>Desactivar pantalla "
                               "\n4=>Activar pantalla "
                               "\n5=>Estado" + "\n"))


OrdenadorCasa = COrdenador('MSI', 'amd', 2.5, 'apagado', 'inactiva')
OrdenadorTrabajo = COrdenador('toshiba', 'amd', 3, 'encendido', 'activa')
OrdenadorCasa.estadoDelOrdenador()
print("----------------------------")
OrdenadorTrabajo.estadoDelOrdenador()
print("----------------------------")

miOrdenador = COrdenador('toshiba', 'amd', 3, 'apagado', 'inactiva')
miOrdenador.menu()
