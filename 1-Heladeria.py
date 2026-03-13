vainilla = 0   
chocolate = 0
fresa = 0

for i in range(5):
    sabor = input ("Ingrese el sabor Que desea (vainilla, chocolate , fresa): ")

    if sabor == "vainilla":
        vainilla = vainilla + 1
    elif sabor == "chocolate":
        chocolate = chocolate + 1 
    elif sabor == "fresa":
        fresa = fresa + 1 
    else:
        print("Sabor no valido")

    print("Pedidos de vainilla", vainilla)
    print("Pedidos de chocolate", chocolate)
    print("Pedidos de fresa", fresa)

