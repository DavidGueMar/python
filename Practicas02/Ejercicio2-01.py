# Programa que cuenta el número de vocales de una frase

frase = input("Introduzca una frase: ")
# contadorA = 0
# contadorE = 0
# contadorI = 0
# contadorO = 0
# contadorU = 0

vocales = {"a":0,"e":0, "i":0, "o":0, "u":0}

for i in frase.lower():
    if i in vocales:
        vocales[i]+=1 # recorre todas las bocales

for k in vocales:
    print(k,vocales[k])

    # if i == 'a':
    #     contadorA += 1
    # elif i == 'e':
    #     contadorE += 1
    # elif i == 'i':
    #     contadorI += 1
    # elif i == 'o':
    #     contadorO += 1
    # elif i == 'u':
    #     contadorU += 1

# print("a=" + str(contadorA)+
#       " e=" + str(contadorE)+
#       " i=" + str(contadorI)+
#       " o=" + str(contadorO)+
#       " u=" + str(contadorU))
# otra forma de hacerlo sin bucles y mas corta
print("----------------------")
print(" a="+str(frase.count('a'))+
      " e="+str(frase.count('e'))+
      " i="+str(frase.count('i'))+
      " o="+str(frase.count('o'))+
      " u="+str(frase.count('u')))
