edad = int(input("Ingrese su edad: "))

if edad < 13:
    print("No puede ingresar al gimnasio")
elif edad >= 13 and edad <=17:
    print("Bienvenido a la clase de juvenil")
elif edad >= 18 and edad <=59:
    print("Bienvenido a la clase general")
else:
    print("Bienvenido a clase senior")
    