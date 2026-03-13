bajo = 0
medio = 0
alto = 0

for i in range(5):
    print(f"\n--- Registro de la persona {i+1} ---")
    
    nombre = input("Nombre: ")
    dias = int(input("Días asistidos en la semana: "))
    minutos = int(input("Minutos promedio por día: "))

    if dias < 3:
        print(f"Estado: {nombre} tiene Bajo compromiso.")
        bajo = bajo + 1 
        
    elif 3 <= dias <= 4:
        print(f"Estado: {nombre} tiene Compromiso medio.")
        medio += 1      
        
    else:  
        print(f"Estado: {nombre} tiene Compromiso alto.")
        alto += 1

print("\n" + "="*30)
print("RESUMEN FINAL DEL GIMNASIO")
print(f"Personas con Bajo compromiso: {bajo}")
print(f"Personas con Compromiso medio: {medio}")
print(f"Personas con Compromiso alto: {alto}")