import os
os.system("cls")

angulo = int(input("Ingrese el número de grados del ángulo: "))

if angulo == 0:
    print("El ángulo es nulo.")
elif 0 < angulo < 90:
    print("El ángulo es agudo.")
elif angulo == 90:
    print("El ángulo es recto.")
elif 90 < angulo < 180:
    print("El ángulo es obtuso.")
elif angulo == 180:
    print("El ángulo es llano.")
elif 180 < angulo < 360:
    print("El ángulo es cóncavo.")
elif angulo == 360:
    print("El ángulo es completo.")
else:
    print("Ingrese otro número válido.")
    