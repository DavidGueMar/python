# programa que guarda preguntas de examen de un modulo
import random


class Examen():

    def __init__(self, modulo):
        self.Modulo = modulo
        self.Preguntas = {"python": [("¿como se hace este exámen?", "no lo se", 3)]}

    def InsertarPregunta(self, pregunta, respuesta, puntuacion, tema="python"):

        # Controlamos que puntuación esté dentro de los límites indicados
        if puntuacion < 0:
            puntuacion = 1
        elif puntuacion > 10:
            puntuacion = 10

        if tema in self.Preguntas:
            self.Preguntas[tema].append((pregunta, respuesta, puntuacion))
        else:
            # print("añadiendo tema")
            self.Preguntas[tema] = [(pregunta, respuesta, puntuacion)]  # se añaden los elementos el diccionario

    def __str__(self):
        mensaje = ''
        for tema in self.Preguntas.keys():
            mensaje += 'Tema: ' + tema + '\n'
            for pregunta in self.Preguntas[tema]:
                mensaje += '\tPregunta' + str(pregunta[0]) + '\n\tRespuesta: ' + \
                           str(pregunta[1]) + '\n\tPuntuacion ' + str(pregunta[2]) + "\n\n"
            mensaje += '\n--------------------------\n'
        return mensaje

    def GenerarExamen(self, tema, nPreguntas):

        if tema in self.Preguntas:
            print("existe ese tema ")
            if len(self.Preguntas[tema]) >= nPreguntas:
                print("Hay preguntas suficientes ")
                listaPreguntas = self.Preguntas[tema]
                maxNota = 0
                notaObtenida = 0
                for i in range(0, nPreguntas):
                    randomIndex = random.randint(0, len(listaPreguntas) - 1)
                    pregunta = listaPreguntas[randomIndex]
                    respuesta = input("Pregunta " + str(i) + ": " + pregunta[0])
                    if respuesta == pregunta[1]:
                        notaObtenida += pregunta[2]
                        print("Respuesta correcta")
                    else:
                        print("Pregunta incorrecta")
                    maxNota += pregunta[2]
                    del listaPreguntas[randomIndex]
            print("Total Preguntas: " + str(nPreguntas) +
                  "\nPuntuación máxima obtenida: " + str(maxNota) +
                  "\nPuntuación obtenida: " + str(notaObtenida))+"\n\n"
        else:
            print("no existe ese tema")


#examen = Examen("dam")
# examen.InsertarPregunta("cuantos años tienes", "tengo 20", 5, "java")
# examen.InsertarPregunta("como te llamas", "juan", 7, "java")
# examen.InsertarPregunta("como te ls", "juan", 7, "java")
# examen.InsertarPregunta("como s", "juan", 7, "java")
# examen.GenerarExamen("java", 2)
opcion = int(input("Introduce el número con la opción deseada:"
                   " \n1. Crear Examen: "
                   "\n2. Introducir Preguntas: "
                   "\n3. Imprimir Preguntas: "
                   "\n4. Generar Examen: "
                   "\n5.Salir:\n"))
while (opcion != 0):
    if (opcion == 1):
        modulo=input("introduce el nombre del modulo que desee: \n")
        examen = Examen(modulo)
    elif (opcion == 2):
        pregunta = input("Escribe la pregunta que deseas insertar: \n")
        respuesta = input("Escribe la respuesta correcta: \n")
        puntuacion = int(input("Introduce la puntuacion: \n"))
        tema = input("Introduce el tema: \n")
        examen.InsertarPregunta(pregunta, respuesta, puntuacion, tema)
    elif (opcion == 3):
        print(examen)  # mostramos lo que tenemos en el diccionario
    elif (opcion == 4):
        tema=input("Introduce el tema sobre que deseas: \n")
        preguntas = int(input("Introduce el número de preguntas: \n"))
        examen.GenerarExamen(tema,preguntas)
    elif (opcion == 5):
        break
    opcion = int(input("Introduce el número con la opción deseada:"
                       " \n1. Crear Examen: "
                       "\n2. Introducir Preguntas: "
                       "\n3. Imprimir Preguntas: "
                       "\n4. Generar Examen: "
                       "\n5.Salir:\n"))
