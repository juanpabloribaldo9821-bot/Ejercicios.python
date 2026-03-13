total_dia = 0

corte = 0
cepillado = 0
tintura = 0

for i in range(7):
    print("Cliente", i + 1)

    nombre = input("Ingrese el nombre del cliente: ")
    servicio = input("Servicio (corte / cepillado / tintura): ")
    valor = float(input("Valor pagado: "))

    total_dia = total_dia + valor

    if servicio == "corte":
        corte = corte + 1
    elif servicio == "cepillado":
        cepillado = cepillado + 1
    elif servicio == "tintura":
        tintura = tintura + 1
    else:
        print("Servicio no valido")

print("Total del dia:", total_dia)

print("Cantidad de corte:", corte)
print("Cantidad de cepillado:", cepillado)
print("Cantidad de tintura:", tintura)

if corte > cepillado and corte > tintura:
    print("El servicio mas solicitado fue: corte")
elif cepillado > corte and cepillado > tintura:
    print("El servicio mas solicitado fue: cepillado")
else:
    print("El servicio mas solicitado fue: tintura")