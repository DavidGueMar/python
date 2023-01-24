# Programa que dada una lista de cadenas, devuelve una lista con las cadenas mas largas
def cadenaMayor():
    lista = []
    aux = ""
    cadena = input("Introduce cualquier letra para comenzar")
    while cadena != "":
        cadena = input("Introduce una cadena: ")
        lista.append(cadena)
        if len(cadena) >= len(aux):
            aux = cadena
            x=lista[-2:]
        print(x)

cadenaMayor()



