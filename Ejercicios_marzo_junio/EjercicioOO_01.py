# Programa que simula el comportamiento de un ordenador

class COrdenador(object):
    def __init__(self,CMarca,CProcesador,CPeso,CEstado,CPantalla):
        self.CMarca=CMarca
        self.CProcesador = CProcesador
        self.CPeso = CPeso
        self.CEstado = CEstado
        self.CPantalla = CPantalla

    def encenderOrdenador(self,):
        if(self.CEstado == "encendido"):
            print("El ordenador ya está encendido")
        else:
            self.CEstado ="encendido"
            self.CPantalla ="activa"
            print("Ordenador "+ self.CEstado+"\npantalla "+self.CPantalla)

    def apagarOrdenador(self):
        if(self.CEstado =="apagado"):
            print("El ordenador ya está apagado")
        else:
            self.CEstado ="apagado"
            self.CPantalla = "inactiva"
            print("Ordenador "+ self.CEstado+"\nPantalla "+self.CPantalla)

    def desactivarPantalla(self):
        if (self.CPantalla == "inactiva"):
            print("La pantalla está desactivada")
        else:
            self.CPantalla="inactiva"
            print("Desacivando pantalla")
            