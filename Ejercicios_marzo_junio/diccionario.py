# Programa que emula el comportamiento de un diccionario

class Diccionario():
    def __init__(self,nombre,editorial,nivel,palabras):
        self.Nombre = nombre
        self.Editorial = editorial
        self.Nivel = nivel
        self.Palabras = palabras
        self.Diccionario = {}

    def crearDiccionario(self):
        pass
    def introducirPalabras(self,palabra,editorial,nivel,acepciones):
        if palabra in self.Diccionario.keys():
            self.Diccionario[palabra].append
        self.Diccionario[palabra]=[(acepciones,editorial,nivel)]
    def introducirAcepciones(self):
        pass
    def consultarPalabras(self):
        pass
    def sacarPalabrasPorletras(self):
        pass