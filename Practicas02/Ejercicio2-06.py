# Programa que calcula los 100 primeros terminos de la sucesión de Fibonacci
sucesion=[0,1]
actual=0
siguiente=1
for n in range(100-1):
    sucesion.append(actual+siguiente)
    aux = actual + siguiente
    actual = siguiente
    siguiente = aux
print(sucesion)