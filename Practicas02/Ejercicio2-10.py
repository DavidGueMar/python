# Programa que emula el juego del ahorcado
import random

vidas = 6
# dibujamos el tablero

# Lista con las palabras que va a incluir el juego
palabras = ["urna", "tubos", "descalzo", "aburrimiento", "lavarropas", "gatito", "dados", "guardaespaldas", "culebra",
            "harina", \
            "afecto", "gorila", "diamante", "inyectar", "multa", "contenedor", "asesinato", "preservativo", "esposo",
            "invitado"]
# seleccionamos la palabra a adivinar, al azar
palabraSecreta = random.choice(palabras)
#print(palabraSecreta)


# lista con las letras introducidas
listaLetrasIntroducidas = []
# mostramos un guión por cada letra que contiene la palabra
print("_" * len(palabraSecreta))

while vidas > 0:
    letraIntroducida = input("Introduce una letra: ")
    if (len(letraIntroducida) != 1 and letraIntroducida.isnumeric()):
        print("Vuelve a intentarlo, deves introducir una sola letra")
    else:
        if letraIntroducida.lower() in listaLetrasIntroducidas:
            print("Ya has introducido esa palabra, prueba otra vez")
        else:
            listaLetrasIntroducidas.append(letraIntroducida)
            if letraIntroducida.lower() in palabraSecreta:
                print("Felicidades has adivinado una letra")

            else:
                vidas -= 1
                print("Has fallado te quedan " + str(vidas) + " Vidas")
    if vidas == 0:
        print("Has perdido la palabra secreta era " + palabraSecreta)
    estatusActual = ""
    letrasFaltantes = 0

    for letra in palabraSecreta:
        if letra in listaLetrasIntroducidas:
            estatusActual = estatusActual + letra
        else:
            estatusActual = estatusActual + "_"
            letrasFaltantes = letrasFaltantes + 1
    print(estatusActual)

    if letrasFaltantes ==0:
        print("Felicidades has ganado")
        print("La palabra secreta es " + palabraSecreta)
        break