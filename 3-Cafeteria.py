bebida = input("Que bebida desea cafe, te ,jugo: ")
cantidad = int(input("Cuantas unidades desea comprar" ))

if bebida == "cafe":
    precio = 4000
elif bebida == "te":
    precio = 3500
elif bebida == "jugo":
    precio = 5000
else:
    print("Bebida no disponible")
    precio = 0

total = precio * cantidad

print("Total a pagar:", total)