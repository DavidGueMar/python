# Programa que simula el comportamiento de una persona

class Persona(object):
    def __init__(self, nif, nombre, apellidos, edad):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def medad(self):
        return self.edad

    def mnombre(self):
        return self.nombre

    def mnif(self):
        return self.nif

    def mapellidos(self):
        return self.apellidos

    def mostrarNombreCompleto(self):  # Muetra los atributos de persona
        print("Nif: " + self.nif + "\n" +
              "Nombre: " + self.nombre + "\n" +
              "Apellidos: " + self.apellidos + "\n" +
              "Edad: " + str(self.edad))


david = Persona("77756394h", "David", "Guerrero", 26)
david.mostrarNombreCompleto()


class Alumno(Persona):  # creamos la clase hija de persona
    def __init__(self, nif, nombre, apellidos, edad,
                 curso):  # Creamos el constructor de la clase especificando los atributos
        self.curso = curso
        Persona.__init__(self, nif, nombre, apellidos,
                         edad)  # Especificamos la clase y llamamos a su constructor  y a sus atriburos

    def mcurso(self):
        return self.curso

    def mostrar(self):  # Esta clase debe mostrar los atributos de la persona y además el curso
        print("Nif: " + self.nif + "\n" +
              "Nombre: " + self.nombre + "\n" +
              "Apellidos: " + self.apellidos + "\n" +
              "Edad: " + str(self.edad) + "\n" +
              "Curso: " + self.curso)
juanico = Alumno("77756394h","Juan","Perez",34,"2ªDam")
juanico.mostrar()