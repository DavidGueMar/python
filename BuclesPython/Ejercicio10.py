# Programa que toma 100 números aleatorios entre 0 y 99 y los muestra dentro de estos intervalos [0-19],[20-39],[40-59],[60-79] y [80-99]
import random

primero = 0
segundo = 0
tercero = 0
cuarto = 0
quinto = 0

for i in range(100):
    n = random.randint(0, 99)

    if n in range(0, 20):
        primero += 1
    elif n in range(20, 40):
        segundo += 1
    elif n in range(40, 60):
        tercero += 1
    elif n in range(60, 80):
        cuarto = cuarto + 1
    elif n in range(80, 100):
        quinto += 1

print("[0 -19]: " + str(primero))
print("[20-39]: " + str(segundo))
print("[40-59]: " + str(tercero))
print("[60-79]: " + str(cuarto))
print("[80-99]: " + str(quinto))
print("Total: " + str((primero + segundo + tercero + cuarto + quinto)))
