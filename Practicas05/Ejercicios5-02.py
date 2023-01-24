#Programa que simula el comportamiento de un coche

class Ccoche(object):
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    def arrancarMotor(self):
        print("Motor arrancado")
        return True
    def acelerar(self):
        if self.arrancarMotor()==True:
            print("Acelerando")
            return True
    def subirMarcha(self):
        if self.acelerar()==True:print("Subiendo marcha")
    def bajarMarcha(self):
        if self.frenar()==True:print("Bajando marcha")
    def frenar(self):
        print("Frenando")
        return True
    def pararMotor(self):
        print("Apagando motor")

coche=Ccoche('Renault','megan','rojo')
coche.arrancarMotor()
coche.acelerar()
coche.subirMarcha()
coche.acelerar()
coche.subirMarcha()
coche.frenar()
coche.bajarMarcha()
coche.frenar()
coche.bajarMarcha()
coche.pararMotor()