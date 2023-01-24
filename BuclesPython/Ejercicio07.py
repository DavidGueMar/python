#programa que pide numeros entero reales, finaliza al introducir un 0 y muestra el numero mayor

num = int(  input("Introduzca un número (cero para terminar): "))

mayor = 0
while num != 0:
    if num > mayor:
        mayor = num
    num = int(  input("Introduzca un número (cero para terminar): "))
print("Mayor: " + str(mayor))