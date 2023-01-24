# Programa que calcula superficíes con un menú que solicita la figura que va a calcular y los datos (lado,base, altura y radio)
import numpy as numpy

numMenu = 0
while numMenu != 4:
    print("Cálculo de superficies:")
    print("1.-Cuadrados")
    print("2.-Triángulos")
    print("3.-Círculos")
    print("4.-Salir")

    numMenu = int(input("Elija opción (1-4): "))
    if numMenu == 1:
        base = float(input("Introduce la base del cuadrado: "))
        areaCuadrado = base * base
        print("El area es :" + str(areaCuadrado) + "cm²")
    elif numMenu == 2:
        base = float(input("introduce base: "))
        altura = float(input("Inroduce altura: "))
        areaTriangulo = (base * altura) / 2
        print("El area es: " + str(areaTriangulo) + "cm²")
    elif numMenu == 3:
        radio = float(input("introduce el radio: "))
        areaCirculo = numpy.pi * (radio * radio)
        print("El area es: " + str(areaCirculo)+ "cm²")
    elif numMenu == 4:
        print("Se acabó")
        continue


