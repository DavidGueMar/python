# programa que comprueba si un dni es válido o no

#funcion que comprueba si el nif es válido

def letra_nif(dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    resto = dni % 23
    print(str(dni) +"-"+ letras[resto])
nif = int(input("Introduce el dni: "))
letra_nif(nif)

