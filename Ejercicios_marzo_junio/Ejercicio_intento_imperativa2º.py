import random

filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))
casillas = filas * columnas


def GenerarMatriz(filas, columnas):
    tablero = []
    for i in range(filas):
        tablero.append([])
        for j in range(columnas):
            numero = random.randint(0, casillas)
            if numero not in tablero[i]:
                tablero[i].append(numero)
            else:
                tablero[i].append(0)

    for i in range(filas):
        for j in range(columnas):
            print("[" + str(tablero[i][j]) + "]", end=" ")
        print()

    return tablero


tablero = GenerarMatriz(filas, columnas)

coordenadaFila = int(input("Introduce la coordenada de la fila"))
coordenadaColumna = int(input("Introduce la coordenada de la columna"))

while ((coordenadaColumna < 0 or coordenadaColumna > columnas) or
       (coordenadaFila < 0 or coordenadaFila > filas)):
    print("Coordenada incorrecta vuelve a introducirlas")
    coordenadaFila = int(input("Introduce la coordenada de la fila"))
    coordenadaColumna = int(input("Introduce la coordenada de la columna"))
print("Las coordenadas son correctas")
coordenada = {}
coordenada["fila"] = coordenadaFila
coordenada["columna"] = coordenadaColumna

print("las coordenadas son ")

# otra forma de mostrar la clave y el valor de un diccionario, en este caso no es necesario el for para ver los valores
print(coordenada.items())

print("La coordenada de la fina es --->" + str(
    coordenada.get('fila')))  # con el método .get obtenemos el valor de una key que escribamos entre comillas

def sumarVecinos(tablero, coordenada):
    #objetivo = tablero[coordenada.get("fila")][coordenada.get("columna")]

    resultado = tablero[coordenada.get("fila")][coordenada.get("columna")] + \
                tablero[coordenada.get("fila")-1][coordenada.get("columna")-1]+ \
                tablero[coordenada.get("fila")+1][coordenada.get("columna")+1]
    print("La suma es "+str(resultado))
    print( "Valor 1 " + str(tablero[coordenada.get("fila")][coordenada.get("columna")]) )
    print( "Valor 2 " + str(tablero[coordenada.get("fila")-1][coordenada.get("columna")-1]) )
    print( "Valor 3 " + str(tablero[coordenada.get("fila")+1][coordenada.get("columna")+1]) )





# EJEMPLO DE POSIBLE RESULTADO PARA SUMAR VECINOS
# def buscaminas(tablero, i, j):
#     minas=0
#     for h in range(i-1, i+2):
#         for v in range(j-1, j+2):
#             if h<0 or h>len(tablero[0])-1 or v<0 or v>len(tablero)-1:
#                 continue
#             minas = minas+1 if tablero[h][v]=="x" else minas
#     return minas
sumarVecinos(tablero,coordenada)
