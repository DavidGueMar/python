# Examen imperativo marzo-junio
# David Guerrero Martinez
import random

count = 0
Concursantes = {}
escenario = []

while (count < 4):
    concursante = input("Introduce el nombre del concursante " + str(count + 1) + ":")
    nacionalidad = input("Introduce la nacionalidad del concursante " + str(count + 1) + ":")

    Concursantes[concursante] = nacionalidad
    count += 1

print("------contenido del cicionario--------------")
print(Concursantes.items())
print("----------------------------------")


def Crear_Escenario(Concursantes):
    escenario = []
    for i in range(4):
        escenario.append([])
        for j in range(4):
            escenario[i].append("X")
            for concursante, nacionalidad in Concursantes.items():
                numero = random.randrange(0, 2)
                if numero == 1:
                    escenario[i].append(concursante)
                # elif numero ==0:
                #     escenario[i].append("X")


                # if concursante == escenario[i]:
                #     escenario[i].append("X")
                # else:
                #     escenario[i].append(concursante)

    for i in range(4):
        for j in range(4):
            print(str(escenario[i][j]), end=" ")
        print()

    return escenario


Crear_Escenario(Concursantes)
Movimientos = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]

print("-------------------------------------------")

for i in range(len(Crear_Escenario(Concursantes)) ):
    for j in range(len(Crear_Escenario(Concursantes))):
        aleatorio = random.randint(0,4)
        if escenario[i]==concursante:
            escenario[i].append(aleatorio)

        print(str(escenario[i][j]), end=" ")
print()
