
import os
os.system("cls")

montototal = float(input("Ingrese monto total vendido: "))


comision = (montototal * 9) / 100
sueldobruto = 500 + comision
descuento = (sueldobruto * 11) / 100
sueldoneto = sueldobruto - descuento

print("Comisión: S/.", format(comision, ".2f"))
print("Sueldo bruto: S/.", format(sueldobruto, ".2f"))
print("Descuento: S/.", format(descuento, ".2f"))
print("Sueldo neto: S/.", format(sueldoneto, ".2f"))
