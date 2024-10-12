
import os
os.system("cls")

donacion = float(input("Ingrese el monto de la donación: "))

centro_de_salud = donacion * 0.25
comedor_infantil = donacion * 0.35
escuela_infantil = donacion * 0.25
asilo_ancianos = donacion * 0.15


print("El centro de salud recibe S/.", format(centro_de_salud, ".2f"))
print("El comedor infantil recibe S/.", format(comedor_infantil, ".2f"))
print("La escuela infantil recibe S/.", format(escuela_infantil, ".2f"))
print("El asilo de ancianos recibe S/.", format(asilo_ancianos, ".2f"))
