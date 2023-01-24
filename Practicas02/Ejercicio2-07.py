# programa que lee una matriz de  5x 5 y calcula la suma de las filas y las columnas

N = int(input("Introduce el tamaño de la matriz"))
arraySumFilas = [0] * N
arraySumColumna = [0] * N
matriz = []

for i in range(N):
    matriz.append(input("Introduce tu fila: ").split()[:N])

for i in range(N):
    for j in range(N):
        matriz[i][j] = int(matriz[i][j])

sumaFilas = 0
sumaColumnas = 0
for i in range(N):
    sumaFilas = 0
    sumaColumnas = 0
    print("")
    for j in range(N):
        print(matriz[i][j], end="")
        sumaFilas += matriz[i][j]
        sumaColumnas += matriz[j][i]

    arraySumFilas[i] = sumaFilas
    arraySumColumna[i] = sumaColumnas
print("\nLa suma de las filas es: ")
for i in range(N):
    print(str(arraySumFilas[i]), " ", end="")

print("\nLa suma de las columnas es: ")

for i in range(N):
    print(str(arraySumColumna[i]), " ", end="")
