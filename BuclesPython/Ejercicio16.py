# Programa que dada una cantidad devuelva el menor número de billetes y monedas

dinero = int ( input("Introduzca una cantidad: "))

if dinero >= 500:
    cantidad = dinero // 500
    print("hay " + str(cantidad) + " billetes de 500 euros")
    dinero = dinero % 500
if dinero >= 200:
    cantidad = dinero // 200
    print("Hay " + str(cantidad) + " billetes de 200")
    dinero = dinero % 200
if dinero >= 100:
    cantidad = dinero // 100
    print("Hay " + str(cantidad) + " billetes de 100")
    dinero = dinero % 100
if dinero >= 50 :
    cantidad = dinero // 50
    print(" Hay " + str(cantidad) + " billetes de 50")
    dinero = dinero % 50
if dinero >= 20:
    cantidad = dinero // 20
    print("Hay " + str(cantidad) + " billetes de 20")
    dinero = dinero % 20
if dinero >= 10:
    cantidad = dinero // 10
    print("Hay " + str(cantidad) + "billetes de 10")
    dinero = dinero % 10
if dinero >= 5:
    cantidad = dinero // 5
    print("Hay " + str(cantidad) + " billetes de 5")
if dinero >= 2 :
    cantidad = dinero // 2
    print("Hay " + str(cantidad) + " monedas de 2")
if dinero >= 1:
    cantidad = dinero // 2
    print("Hay " + str(cantidad) + " monedas de 1")

# Otra forma de hacerlo

dinero2 = int ( input("Introduzca una cantidad: "))

lista = [500,200,100,50,20,10,5,2,1]
for i in lista:
    if dinero2 > i:
        cantidad = dinero2 // i
        print("Hay " + str(cantidad) + (' billete' if dinero2 >= 5 else ' moneda') +('s' if cantidad > 1 else ' ') +" de " + str(i) + " euros")
        dinero2 = dinero2 % i