# Programa que calcula la letra del dni

def letra_dni(x):
    letras = {"T": 0, "R": 1, "W": 2, "A": 3, "G": 4, "M": 5, "Y": 6,
              "F": 7, "P": 8, "D": 9, "X": 10, "B": 11, "N": 12,
              "J": 13, "Z": 14, "S": 15, "Q": 16, "V": 17,
              "H": 18, "L": 19, "C": 20, "K": 21, "E": 22}

    resto = x % 23

    if resto in letras.values():  # forma de saber si un valor existe en un diccionario
        print("Tu letra existe")
    else:
        print("Tu letra no existe")

    # forma de obtener la clave correspondiente a un valor en un diccionario
    print("La letra de tu DNI es: " + list(letras.keys())[
        list(letras.values()).index(resto)])  # Le pasamos la variable resto al index y si la encuentra la imprime


NumeroDNI = int(input("Introduce tu número de DNI completo: "))
letra_dni(NumeroDNI)
