import os

os.system("cls")


horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
tarifa_horaria = float(input("Ingrese la tarifa horaria: "))

sueldo_basico = tarifa_horaria * horas_trabajadas
bonificacion = sueldo_basico * 0.20
sueldo_bruto = sueldo_basico + bonificacion
descuento = sueldo_bruto * 0.10
sueldo_neto = sueldo_bruto - descuento

print("")
print("Sueldo básico: S/.", format(sueldo_basico, ".2f"))
print("Sueldo bruto : S/.", format(sueldo_bruto, ".2f"))
print("Sueldo Neto  : S/.", format(sueldo_neto, ".2f"))