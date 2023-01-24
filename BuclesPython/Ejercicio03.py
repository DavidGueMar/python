# Ejercicio que lee notas de alumnos y dice cuantos aprobados y la nota media

print("Introduzca las notas, ENTER para terminar")

contador = 0
aprobados = 0
suspensos = 0
media = 0
nota = input("Nota del alumno " + str(contador + 1) + ": ")
while nota != "":
    nota = float(nota)

    contador += 1
    if nota >= 5:
        aprobados += 1
    else:
        suspensos += 1

    media += nota
    nota = input("Nota del alumno " + str(contador + 1) + ": ")

print("Numero de alumnos: " + str(contador) +
      "\nAprobados: " + str(aprobados) +
      "\nSuspensos: " + str(suspensos) +
      "\nNota media: " + str(media / contador))
