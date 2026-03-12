contador = 0          
i = 1                 

while i <= 6:         
    precio = int(input(f"Ingresa el precio del producto {i}: "))
    
    if precio > 100000:  
        contador += 1     
    
    i += 1

    print("Cantidad de productos que cuestan más de 100000:", contador)