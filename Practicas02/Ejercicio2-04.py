# Programa que pide nombres y los muestra ordenados
nombres = input("Introduce nomnbres. ENTER para terminar:\n")
listaNombres=[]
while nombres != "":
    listaNombres.append(nombres)
    nombres = input()
listaNombres.sort()
print("Los nombres son: ")
for nombres in listaNombres:
    print(nombres)