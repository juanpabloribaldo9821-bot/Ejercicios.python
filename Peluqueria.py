hora = int(input("Hora de llegada formato 0 a 23: "))

if hora >= 6 and  hora <= 11:
    print("Buenos dias")
elif hora >= 12 and hora <= 17:
    print("Buenas tardes")
elif hora >= 17 and hora <= 22:
    print("Buenas noches")
else:
    print("Fuera de horario")

