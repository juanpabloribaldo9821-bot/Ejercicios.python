bajo = 0
medio = 0
alto = 0

suma_promedios = 0

mejor_promedio = 0
mejor_nombre = ""

n = int(input("Cuantos estudiantes va a registrar: "))

for i in range(n):
    print("Estudiante", i + 1)

    nombre = input("Nombre: ")
    speaking = float(input("Nota speaking: "))
    listening = float(input("Nota listening: "))
    reading = float(input("Nota reading: "))

    promedio = (speaking + listening + reading) / 3
    print("Promedio:", promedio)

    suma_promedios = suma_promedios + promedio

    if promedio < 60:
        bajo = bajo + 1
    elif promedio >= 60 and promedio <= 79:
        medio = medio + 1
    else:
        alto = alto + 1
 
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_nombre = nombre

promedio_general = suma_promedios / n

print("Promedio general del grupo:", promedio_general)

print("Mejor estudiante:", mejor_nombre)
print("Mejor promedio:", mejor_promedio)

print("Cantidad nivel bajo:", bajo)
print("Cantidad nivel medio:", medio)
print("Cantidad nivel alto:", alto)