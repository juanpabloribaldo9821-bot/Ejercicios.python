total_dia = 0

while True:
    print("\n--- NUEVO PEDIDO (Escribe 'salir' en el nombre para terminar el día) ---")
    nombre = input("Nombre del cliente: ")
    
    if nombre.lower() == "salir":
        break  

    total_cliente = 0
    
    print("Menú: café (4000), capuchino (7000), pastel (6000)")
    
   
    cant_cafe = int(input("¿Cuántos cafés? "))
    cant_capu = int(input("¿Cuántos capuchinos? "))
    cant_pastel = int(input("¿Cuántos pasteles? "))


    subtotal = (cant_cafe * 4000) + (cant_capu * 7000) + (cant_pastel * 6000)

    if subtotal > 20000:
        descuento = subtotal * 0.10
        total_cliente = subtotal - descuento
        print(f"¡Descuento del 10% aplicado! Ahorraste: {descuento}")
    else:
        total_cliente = subtotal
        print("No aplica descuento.")

    print(f"Total a pagar por {nombre}: {total_cliente}")
    total_dia = total_dia + total_cliente

print("\n" + "="*30)
print(f"VENTAS TOTALES DEL DÍA: {total_dia}")
print("==============================")