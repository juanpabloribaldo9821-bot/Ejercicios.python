
horas = int(input("Cada hora adicional: "))

if horas == 1:
    total = 5000
else:
     total = 5000 + (horas - 1) * 3000
print ("total a pagar:", total)


