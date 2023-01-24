# Programa que dada una cantidad de vuelve el menor número de billetes y monedas de curso legal
dinero2 = int ( input("Introduzca una cantidad: "))

lista = [500,200,100,50,20,10,5,2,1]
for i in lista:
    if dinero2 > i:
        cantidad = dinero2 // i
        print("Hay " + str(cantidad) + (' billete' if dinero2 >= 5 else ' moneda') +('s' if cantidad > 1 else ' ') +" de " + str(i) + " euros")
        dinero2 = dinero2 % i