# programa que lee notas de alumnos, hasta pulsar enter y muestra las notas, los aprobados los suspensos y la nota media
print("Introduzca las notas, ENTER para terminar:")
nAlumno = 1
aprobados = 0
suspensos = 0
nota = input("Nota del alumno " + str(nAlumno) + ":")
media = 0
notasAlumnos = {}  # creamos el diccionario
while nota != "":
    nota = float(nota)  # convertimos nota en un float
    if nota < 5:  # si nota es menor que 5
        suspensos += 1  # añadimos 1 a los suspensos
    else:
        aprobados += 1  # si no, lo añadimos a aprobados
    media += nota  # vamos metiendo todas las notas en esta variable para que se sumen
    notasAlumnos[nAlumno] = nota  # declaramos que el alumno va a se la clave y la nota el valor del diccionario
    nAlumno += 1  # aumentamos el número del alumno como un contador
    nota = input("Nota del alumno " + str(nAlumno) + ":")  # nos vuelve a pedir la nota hasta que le metamos un caracter vacío
print("Se han introducido las siguientes notas: ")
for key in notasAlumnos:  # como el diccionario es iterable se puede recorrer de esta manera
    print(
        'Alumno {0}: {1}'.format(key, notasAlumnos[key]))  # lo imprimimos formateado para que salga la nota y el alumno
print("\nNúmero de alumnos:" + str(nAlumno - 1) +
      "\nAprobados: " + str(aprobados) +
      "\nSuspensos: " + str(suspensos) +
      "\nNota media: " + str(media / (nAlumno - 1)))
