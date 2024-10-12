import os
os.system("cls")

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

numero_intermedio = None


if (numero1 > numero2 and numero1 < numero3) or (numero1 < numero2 and numero1 > numero3):
    numero_intermedio = numero1
elif (numero2 > numero1 and numero2 < numero3) or (numero2 < numero1 and numero2 > numero3):
    numero_intermedio = numero2
elif (numero3 > numero1 and numero3 < numero2) or (numero3 < numero1 and numero3 > numero2):
    numero_intermedio = numero3

if numero_intermedio is not None:
    print("El número intermedio es:", numero_intermedio)
else:
    print("No hay un número intermedio único.")
