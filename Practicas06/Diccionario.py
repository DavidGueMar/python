# Programa que sumila el comportamiento de un diccionario que oculta palabras
import math
import random


class Secreto(object):
    def __init__(self, TamañoMax=10):
        self.TamañoMax = TamañoMax
        self.Lista_Cadenas = []
        self.Dic_Palabras = {}

    def InsertarCadena(self, cadena):
        self.Lista_Cadenas.append(cadena)
        for cadena in self.Lista_Cadenas:
            if cadena in self.Dic_Palabras.values():
                print("La palabra ya está en el diccionario")
                return False
            else:
                self.Dic_Palabras[cadena] = random.randint(1,10)
                return True

    def __str__(self):
        palabras = list(self.Dic_Palabras.values())  # obtenemos la lsita de las palabras en el diccionario
        palabras.sort()  # la ordenamos
        cadena = "Palabra: {0} Clave--> {1}".format(self.Dic_Palabras.values(), self.Dic_Palabras.keys())
        return cadena

    def OcultarCadena(self, cadena):
        Lista_cadenas = []
        Lista_cadenas.append(cadena)
        for i in range(len(Lista_cadenas)):
            if Lista_cadenas[i] == self.Dic_Palabras.keys():
                Lista_cadenas.append(self.Dic_Palabras.keys()[i])

        return Lista_cadenas

    def ComprobarPalabra(self, palabra):
        for key in self.Dic_Palabras:
            if key == palabra:
                print("La palabra está en el diccionario")
                return True
            else:
                print("no se ha introducido nunca esa palabra")
                return False


secreto = Secreto()
opcion = int(input("1. INtroducir cadena a Secreto\n"
                   "2. Sacar palabras secretas ordenadas alfabéticamente\n"
                   "3. Ocultar cadena\n"
                   "4. Comprobar palabra\n"
                   "0. Salir"))
while (opcion != 0):
    if opcion == 1:
        cadena = input("Introduce la cadena a insertar: ")
        secreto.InsertarCadena(cadena)
    elif opcion == 2:
        secreto.__str__()
    elif opcion == 3:
        cadena = input("introduce la cadena a ocultar: ")
        secreto.OcultarCadena(cadena)
    elif opcion == 4:
        palabra = input("Introduce palabra a comprobar")
        secreto.ComprobarPalabra(palabra)
    opcion = int(input("1. INtroducir cadena a Secreto\n"
                       "2. Sacar palabras secretas ordenadas alfabéticamente\n"
                       "3. Ocultar cadena\n"
                       "4. Comprobar palabra\n"
                       "0. Salir\n"))
