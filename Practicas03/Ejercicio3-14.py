# Programa que realiza operaciones dado un operador y unos datos
def suma(num1,num2):
      sum =  num1 + num2
      return sum
def resta(num1,num2):
      rest= num1 - num2
      return rest
def multiplicacion(num1,num2):
      mult = num1 * num2
      return mult
def division(num1,num2):
      div = num1 / num2
      return div
def absoluto (num):
      absol = abs(num)
      return absol



opcion = input("Elige opción o enter para terminar: \n1.-Suma"
      "\n2.-Resta"
      "\n3.-Multiplicación"
      "\n4.-División"
      "\n5.-Valor absoluto"
      "\n6.-Ecuación de segundo grado\n")
while opcion != "":
      if opcion =="1":
            num1 = int(input("introduce el primer digito"))
            num2 = int(input("introduce elsegundo"))
            print(suma(num1,num2))
      if opcion =="2":
            num1 = int(input("introduce el primer digito"))
            num2 = int(input("introduce elsegundo"))
            print(resta(num1, num2))
      if opcion =="3":
            num1 = int(input("introduce el primer digito"))
            num2 = int(input("introduce elsegundo"))
            print(multiplicacion(num1, num2))
      if opcion =="4":
            num1 = int(input("introduce el primer digito"))
            num2 = int(input("introduce elsegundo"))
            print(division(num1, num2))
      if opcion =="5":
            num = int(input("Introduce el número"))
            print(absoluto(num))
      if opcion =="6":
            print("ha pulsado 6")
      opcion = input("Elige opción o enter para terminar: \n1.-Suma"
                     "\n2.-Resta"
                     "\n3.-Multiplicación"
                     "\n4.-División"
                     "\n5.-Valos absoluto"
                     "\n6.-Ecuación de segundo grado\n")