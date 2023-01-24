# programa que solicita un número y calcula todos
# los números pares entre cero y el número solicitado

num = int(input("Introduce un numero: "))
iterador = 0
sum = 0
if num > 0:
    while iterador <= num:
        if iterador % 2 == 0:
            sum += iterador
        iterador += 1
    print("Los numeros pares son: " + str(sum))

else:
    print("El numero debe ser positivo")
