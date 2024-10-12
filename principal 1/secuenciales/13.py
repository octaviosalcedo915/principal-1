import os, math
os.system("cls")

cateto_a = float(input("Ingrese la longitud del primer cateto (a): "))
cateto_b = float(input("Ingrese la longitud del segundo cateto (b): "))

hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)


print(f"La hipotenusa del triángulo es: {hipotenusa:.2f}")