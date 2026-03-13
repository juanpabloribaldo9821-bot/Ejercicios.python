
dinero_total = 0
cuenta_clientes = 0

c_cono = 0
c_vaso = 0
c_banana = 0

while True:
    producto = input("Producto (cono, vaso, banana) o 'salir': ")

    if producto == "salir":
        break  

    cantidad = int(input("¿Cuántos?: "))

    
    if producto == "cono":
        total_pedido = 3000 * cantidad
        c_cono = c_cono + cantidad 
    elif producto == "vaso":
        total_pedido = 4000 * cantidad
        c_vaso = c_vaso + cantidad 
    elif producto == "banana":
        total_pedido = 9000 * cantidad
        c_banana = c_banana + cantidad 
    else:
        print("Ese sabor no existe.")
        continue 


    print("Total de este cliente:", total_pedido)
    dinero_total = dinero_total + total_pedido
    cuenta_clientes = cuenta_clientes + 1

print("Dinero total:", dinero_total)
print("Clientes:", cuenta_clientes)

if c_cono > c_vaso and c_cono > c_banana:
    print("El más vendido fue: Cono")
elif c_vaso > c_banana:
    print("El más vendido fue: Vaso")
else:
    print("El más vendido fue: Banana Split")




