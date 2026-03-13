total_recaudado = 0
cuenta_carros = 0
cuenta_motos = 0

pago_mas_alto = 0
placa_mas_cara = ""


for i in range(8):
    print(f"\n--- Registro del Vehículo {i+1} ---")
    
    placa = input("Placa del vehículo: ")
    tipo = input("Tipo (carro / moto): ").lower()
    horas = int(input("Horas parqueado: "))

    if tipo == "carro":
        pago_actual = horas * 4000
        cuenta_carros = cuenta_carros + 1
    elif tipo == "moto":
        pago_actual = horas * 2000
        cuenta_motos = cuenta_motos + 1
    else:
        print("Tipo no válido, se cobrará como moto por defecto.")
        pago_actual = horas * 2000

    print(f"Total a pagar por este vehículo: ${pago_actual}")

   
    total_recaudado = total_recaudado + pago_actual
 
    if pago_actual > pago_mas_alto:
        pago_mas_alto = pago_actual
        placa_mas_cara = placa

print("\n" + "="*30)
print("REPORTE DEL PARQUEADERO")
print(f"Total recaudado: ${total_recaudado}")
print(f"Cantidad de carros: {cuenta_carros}")
print(f"Cantidad de motos: {cuenta_motos}")
print(f"El vehículo que más pagó fue la placa {placa_mas_cara} con ${pago_mas_alto}")
print("="*30)
