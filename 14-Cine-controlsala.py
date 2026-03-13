capacidad = int(input("Cual es la capacidad total de la sala: "))

niños = 0
adultos = 0
mayores = 0
total_ingresados = 0

while total_ingresados < capacidad:
    print(f"\nAsientos ocupados: {total_ingresados} / {capacidad}")
    print("Escriba '0' en la edad para dejar de registrar.")
    
    edad = int(input("Ingrese la edad de la persona: "))

    if edad == 0:
        break

    if edad < 13:
        print("Clasificación: Niño")
        niños = niños + 1
    elif edad < 60:
        print("Clasificación: Adulto")
        adultos = adultos + 1
    else:
        print("Clasificación: Adulto mayor")
        mayores = mayores + 1

    total_ingresados = total_ingresados + 1

print("\n" + "="*30)
print("INFORME FINAL DEL CINE")
print(f"Total de personas que entraron: {total_ingresados}")
print(f"Niños: {niños}")
print(f"Adultos: {adultos}")
print(f"Adultos mayores: {mayores}")

if total_ingresados == capacidad:
    print("ESTADO: La sala está LLENA.")
else:
    print(f"ESTADO: La sala NO se llenó. Quedaron {capacidad - total_ingresados} asientos libres.")