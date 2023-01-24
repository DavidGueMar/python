# Programa con varias funciones que hacen de utilidades con alumnos y sus notas
alumnos = ["Ana pi","Pau López","Luis Sol","Mar Vega","Paz Mir"]
notas = [10,5.5,2.0,8.5,7.0]
#alumno_buscado = input("Introduce el nombre del alumno a buscar")

def muestra_nota_de_alumno(alumnos,notas,alumno_buscado):
    for i in range(len(alumnos)):
        if alumnos[i] == alumno_buscado:#si por ejemplo lo encuentra en alumnos[1]
            print(alumno_buscado, notas[i])# aquí imprime notas[1] por que la variable i vale 1 dentro del bucle for



def estudiantes_aprobados(alumnos,notas):
    print("Los alumnos aprobados son: ")
    for i in range(len(notas)):
        if notas[i]>= 5:
            print(alumnos[i] +" -> "+ str(notas[i]))

def numero_aprobados(notas):
    aprobados = 0
    print("El número de alumnos aprobados es: ")
    for i in range(len(notas)):
        if notas[i]>=5:
            aprobados+=1
    print(aprobados)

def estudiantes_con_maxima_nota(alumnos, notas):
    print("Estudiante/s con la nota máxima: ")
    for i in range(len(notas)):
        if notas[i]==10:
            print(alumnos[i])
def alumnos_por_encima_de_la_media(alumnos,notas):
    contador = 0
    aux =0
    media = 0
    for i in range(len(notas)):
        contador+=1
        aux +=notas[i]
    media = aux /contador
    print(media)

    for i in range(len(notas)):
        if notas[i]>=media:
            print("Los alumnos por ecima de la media "+alumnos[i]+" "+str(notas[i]) );

def encontrar_nota_estudiantes(alumnos, notas, alumno_buscado):
    for i in range(len(alumnos)):
        if alumnos[i] == alumno_buscado:
            cadenaAlumno = "La nota del alumno " +alumnos[i]+" es " + str(notas[i])
            return cadenaAlumno
            #print(cadenaAlumno)
        else:
            return None


def menu():
    opcion = -1



#muestra_nota_de_alumno(alumnos,notas, alumno_buscado)
#estudiantes_aprobados(alumnos,notas)
#numero_aprobados(notas)
#estudiantes_con_maxima_nota(alumnos,notas)
#alumnos_por_encima_de_la_media(alumnos,notas)
#print (encontrar_nota_estudiantes(alumnos,notas,"Ana pi"))# Para que que se muestre por pantalla el return de un método hay que meterlo dentro de un print
