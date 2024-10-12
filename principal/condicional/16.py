import os
os.system("cls")

ingresomensual = float(input("Ingrese el ingreso mensual del comprador: S/. "))
costocasa = float(input("Ingrese el costo de la casa: S/. "))

cuotainicial = 0
cuotamensual = 0

if ingresomensual < 1250:
    cuotainicial = costocasa * 0.15  
    cuotamensual = (costocasa - cuotainicial) / 120  
else:
    cuotainicial = costocasa * 0.30  
    cuotamensual = (costocasa - cuotainicial) / 75  


print("La cuota inicial es: S/.", format(cuotainicial, ".2f"))
print("La cuota mensual es: S/.", format(cuotamensual, ".2f"))