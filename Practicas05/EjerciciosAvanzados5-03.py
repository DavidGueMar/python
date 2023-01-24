# Programa que simula el comportamiento de un videoclub

class Socio(object):
    def __init__(self, dni, nombre, telefono, domicilio):
        self.dni = dni
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio

    def __str__(self):
        return 'DNI: {0}\nNombre: {1}\nTeléfono: {2}\nDomicilio: {3}\n'.format(self.dni, self.nombre, self.telefono,
                                                                               self.domicilio)


class Peliculas(object):
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero
        self.alquilada = None

    def __str__(self):
        cadena = "Titulo: {0}\nGenero: {1}\n".format(self.titulo, self.genero)
        if self.alquilada == None:
            cadena = cadena + "Disponible\n"
        else:
            cadena = cadena + "Alquilada a:{0\n}".format(self.alquilada)
        return cadena


class Videoclub:
    def __init__(self):
        self.socios = []
        self.peliculas = []

    def menu(self):
        print('** VIDEOCLUB **')
        print('1) Dar de alta a un nuevo socio')
        print('2) Dar de baja un socio')
        print('3) Dar de alta una pelicula')
        print('4) Dar de baja una pelicula')
        print('5) Alquiler de pelicula')
        print('6) salir')
        opcion = int(input('Escoge una opción (entre 1 y 6): '))
        return opcion

    # Bloque que da de alta a los socios
    def nuevo_socio(self):  # Se introducen los datos del socio
        dni = input("DNI: ")
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        domicilio = input("Domicilio: ")
        return Socio(dni, nombre, telefono, domicilio)

    def contiene_socio(self, dni):  # Este modulo busca los dni en la lista de socios y devuelve true si lo encuentra
        for socio in self.socios:
            if socio.dni == dni:
                return True
        return False

    def alta_socio(self, socio):  # Este modulo añade los socios creados en el otro mo
        self.socios.append(socio)

    def baja_socio(self, dni):  # Este modulo busca los socios y si lo encuentra lo elimina
        for i in range(len(self.socios)):
            if self.socios[i].dni == dni:
                del self.socios[i]
                break

    # Bloque que da de alta a las peliculas
    def nueva_pelicula(self):
        titulo = input("Titulo: ")
        genero = input("Genero: ")
        return Peliculas(titulo, genero)

    def contiene_pelicula(self, titulo):
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                return True
        return False

    def alta_pelicula(self, titulo):  # este bloque añade la pelicula del titulo que le pasemos a la lista
        self.peliculas.append(pelicula)

    def baja_pelicula(self, titulo):
        for i in range(len(self.peliculas)):
            if self.peliculas[i].titulo == titulo:
                del self.peliculas[i]
                break

    # bloque de alquiler de pelicula
    def alquilar_pelicula(self, titulo, dni):
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                if pelicula.alquilada == None:
                    pelicula.alquilada = dni
                    break


videoclub = Videoclub()

opcion = videoclub.menu()

while opcion != 6:
    if opcion == 1:
        print('Alta de socio')
        socio = videoclub.nuevo_socio()
        if videoclub.contiene_socio(socio.dni):
            print('Ya existe un socio con DNI' + socio.dni)
        else:
            videoclub.alta_socio(socio)

    elif opcion == 2:
        print("Baja de socio")
        dni = input("Dni: ")
        if videoclub.contiene_socio(dni):
            videoclub.baja_socio(dni)
            print('socio con DNI ', dni, "dado de baja ")
        else:
            print("No existe ningún socio con DNI" + dni)
        continue
    elif opcion == 3:
        print("Alta de película")
        pelicula = videoclub.nueva_pelicula()
        if videoclub.contiene_pelicula(pelicula.titulo):
            print("Ya hay un ajpelícula con titulo", pelicula.titulo)
        else:
            videoclub.alta_pelicula(pelicula)

    elif opcion == 4:
        print("Baja de pelicula")
        titulo = input("Titulo: ")
        if videoclub.contiene_pelicula(titulo):
            videoclub.baja_pelicula(titulo)
        else:
            print("No existe nunguna pelicula llamada:", titulo)

    elif opcion == 5:
        print("Alquiler de pelicula")
        titulo = input("Titulo de la pelicula: ")
        dni = input("Dni del socio: ")
        hay_pelicula = videoclub.contiene_pelicula(titulo)
        hay_socio = videoclub.contiene_socio(dni)
        if hay_pelicula and hay_socio:
            if videoclub.alquilar_pelicula(titulo, dni):
                print("Operación realizada")
        else:
            if not hay_pelicula:
                print("No hay pelicula titulada: ", titulo)
            if not hay_socio:
                print("No hay socio con DNI: ", dni)

    opcion = videoclub.menu()
