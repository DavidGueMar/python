# Programa que emula el comportamiento de una multinacional
FEMPLE = [[1, "pepe", "A", "Francia"], [2, "juan", "B", "España"], [3, "manolo", "C", "España"]]
empleCategoria = 0

# obtenemos la información de los empleados
# Número total de empleados por categoría
for e in FEMPLE:
    if e[2] == "A":
        empleCategoria += 1

print("Número total de empleados en esa categoría " + str(empleCategoria))
# Número total de empleados por pais
emplePais = 0
for i in FEMPLE:
    if i[3] == "Francia":
        emplePais += 1

print("Número total de empleados en ese país " + str(emplePais))

# País con mayor número de empleados
pais1 = 0
pais2 = 0
pais3 = 0
mayorPais = ""

for j in FEMPLE:
    if j[3] == "Francia":
        pais1 += 1
    elif j[3] == "España":
        pais2 += 1
    elif j[3] == "Portugal":
        pais3 += 1

if pais1 > pais2 and pais1 > pais3:
    mayorPais = pais1
    print("El país con mas empleados es " + j[3] + " con " + str(pais1) + " empleados")
elif pais2 > pais1 and pais2 > pais3:
    mayorPais = pais2
    print("El país con mas empleados es " + j[3] + " con " + str(pais2) + " empleados")
else:
    mayorPais = pais3
    print("El país con mas empleados es " + j[3] + " con " + str(pais3) + " empleados")

