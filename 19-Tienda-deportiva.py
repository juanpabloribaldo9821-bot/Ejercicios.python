agotado = 0
stock_bajo = 0
stock_normal = 0

for i in range(10):
    print("Producto", i + 1)

    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Cantidad disponible: "))

    if cantidad == 0:
        agotado = agotado + 1
    elif cantidad >= 1 and cantidad <= 5:
        stock_bajo = stock_bajo + 1
    else:
        stock_normal = stock_normal + 1

print("Productos agotados:", agotado)
print("Productos con stock bajo:", stock_bajo)
print("Productos con stock normal:", stock_normal)