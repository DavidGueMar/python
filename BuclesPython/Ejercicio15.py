# Programa que dibuja un rombo pidiendo un número entre 2 y 40
nivel = int(input("\nNivel: "))
if nivel >= 2 and nivel <= 40:
    for i in range(nivel +1):
        for j in range ( nivel-i):
            print(" ",end="")
        for k in range(2*i-1):
            print("x",end="")
        print("")
    for i in range(nivel-1,0,-1):
        for j in range(nivel-i):
            print(" ",end="")
        for k in range(2*i-1):
            print("x",end="")
        print("")
elif nivel < 2 or nivel > 4:
    print("El triangulo debe ser mayor que 2 y menor que 40")