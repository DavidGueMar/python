# Programa que imprime un triangulo insertándole un número entre 2 y 40

nivel = int (input("Nivel: "))
equis = 'x'
espacios = ' '
if nivel >= 2 and nivel <= 40:
      for i in range (nivel +1):
         espacios = nivel -i
         print(' '*espacios+'x '*i)
elif nivel < 2 or nivel > 40:
   print("El triangulo debe ser mayor que 2 y menor que 40")

