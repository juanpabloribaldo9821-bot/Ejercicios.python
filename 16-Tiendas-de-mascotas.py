alimento = 0
juguete = 0
accesorio = 0

for i in range(10):
    print("Venta", i + 1)

    categoria = input("Ingrese la categoria (alimento / juguete / accesorio): ")
    valor = float(input("Ingrese el valor de la compra: "))

    if categoria == "alimento":
        alimento = alimento + valor
    elif categoria == "juguete":
        juguete = juguete + valor
    elif categoria == "accesorio":
        accesorio = accesorio + valor
    else:
        print("Categoria no valida")

print("Total vendido en alimento:", alimento)
print("Total vendido en juguete:", juguete)
print("Total vendido en accesorio:", accesorio)

if alimento > juguete and alimento > accesorio:
    print("La categoria que mas dinero genero fue: alimento")
elif juguete > alimento and juguete > accesorio:
    print("La categoria que mas dinero genero fue: juguete")
else:
    print("La categoria que mas dinero genero fue: accesorio")