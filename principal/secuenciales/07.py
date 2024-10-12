import os
os.system("cls")

base_r = float(input("Ingrese la base del rectángulo: "))
altura_r = float(input("Ingrese la altura del rectángulo: "))

area_r = base_r * altura_r            
perimetro_r = 2 * (base_r + altura_r) 

print("El área del rectángulo es:", format(area_r, ".2f"))
print("El perímetro del rectángulo es:", format(perimetro_r, ".2f"))