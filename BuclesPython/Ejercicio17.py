# Programa que adivina un número entre 0 y 100

x: int = 8
izq = 0
der = len(list(range(0, 100)))

while izq <= der:
    medio = (izq + der) / 2
    print("izq: " + str(izq) + " Der: " + str(der) + " medio: " + str(medio))
    if list[medio] == x:
        print("Lo he encontrado1")
    elif medio > x:
        der = medio - 1
        if medio == x:
            print("Lo he encontrado2")
    else:
        izq = medio + 1
        print("lo he encontrado {:.0f}".format(medio))
else:
    ("Valor no encontrado")
