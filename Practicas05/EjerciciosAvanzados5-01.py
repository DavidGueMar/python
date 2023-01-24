# Programa que simula el funcionamiento de un diccionario

class Diccionario(object):
    def __str__(self, nombre, editorial, nivel, **palabras):
        self.nombre = nombre
        self.editorial = editorial
        self.nivel = nivel
        self.palabras=palabras
    def crearDiccionario(**kwargs):
        kwargs={"Caminar":"Acción de moverse", "Correr":"Caminar pero mas rápido"}
        for key, value in kwargs.items():
            print("%s ==%s" %(key,value))
    def introducirPalabras(self):
        palabra= input("Introduce la palabra que quieres añadir al diccionario")
        acepcion= input("Introduce la acepción que queires añadir al diccionario")
        self.crearDiccionario(palabra,acepcion)
    def introducirAcepciones(self):
        pass
    def consultar(self):
        pass
    def sacarPalabras(self):
        pass

diccionario = Diccionario
opcion= int(input("Introduce una opción\n "
                  "1.-Crear Diccionario \n "
                  "2.-Introducir palabras \n "
                  "3.-Introducir acepción \n "
                  "4.-Consulrtar \n "
                  "5.-Sacar palabras \n "
                  "0.- Finalizar programa \n"))

while(opcion!= 0):
    if opcion ==1:
        diccionario.crearDiccionario()
    elif opcion ==2:
        diccionario.introducirPalabras()
    elif opcion ==3:
        diccionario.introducirAcepciones()
    elif opcion==4:
        diccionario.consultar()
    elif opcion==5:
        diccionario.sacarPalabras()
    else:print("La opción elegida no es correcta")

    opcion = int(input("Introduce una opción\n "
                       "1.-Crear Diccionario \n "
                       "2.-Introducir palabras \n "
                       "3.-Introducir acepción \n "
                       "4.-Consulrtar \n "
                       "5.-Sacar palabras \n "
                       "0.- Finalizar programa \n "))