# programa que muestra un menú pudiendo elegir en el dos juegos distintos
import random


class juegos():
    def Tesoro(self, dificultad):
        tablero = []
        filas = 3
        columnas = 4
        aciertos = 0
        fallos = 0
        self.dificultad = dificultad
        if self.dificultad == "facil":
            self.dificultad = 10
        elif self.dificultad == "medio":
            self.dificultad = 6
        elif self.dificultad == "dificil":
            self.dificultad = 4
        while (fallos < self.dificultad):
            for i in range(filas):
                tablero.append([])
                for j in range(columnas):
                    numero = random.randrange(0, 2)
                    if numero == 1:
                        numero = "X"
                    tablero[i].append(numero)

            for i in range(filas):
                for j in range(columnas):
                    print(tablero[i][j], end=" ")
                print()

            filaElegir = int(input("Introduce posicion en la fila: "))
            columnaElegir = int(input("Introduce la posición en la columna: "))
            if (tablero[filaElegir][columnaElegir] == "X"):
                print("Has acertado")
                aciertos += 1
            else:
                print("Has fallado")
                fallos += 1
        print("Has fallado, sólo has acertado " + str(aciertos) + " veces\n¡¡FIN DEL JUEGO!!")
        for i in range(filas):
            for j in range(columnas):
                print(tablero[i][j], end=" ")
            print()

    def BuscarParejas(self):
        return ("DAM", "DAW", "ASIR")

    def GenerarMatriz(self, Lista_Parejas):
        matriz = []
        filas = 4
        columnas = 5
        self.Lista_Parejas = Lista_Parejas
        for i in range(filas):
            matriz.append([])
            for j in range(columnas):
                matriz[i].append(self.Lista_Parejas)
        for i in range(filas):
            for j in range(columnas):
                print(matriz[i][j], end=" ")
            print()


juego = juegos()
# juego.BuscarParejas()
# argus = ("DAM", "DAW", "ASIR")
# juego.GenerarMatriz(*argus)

opcion = int(input("0. Salir"
                   "\n1. Tesoro"
                   "\n2. Busca parejas"
                   "\nTeclee la opción: "))
while (opcion != 0):
    if opcion == 1:
        dificultad = input("Introduzca dificultad:\nfacil\nmedio\ndificil")
        juego.Tesoro(dificultad)
    elif opcion == 2:
        argus = ("DAM", "DAW", "ASIR")
        juego.GenerarMatriz(*argus)

    else:
        break
    opcion = int(input("0. Salir"
                       "\n1. Tesoro"
                       "\n2. Busca parejas"
                       "\nTeclee la opción: "))
