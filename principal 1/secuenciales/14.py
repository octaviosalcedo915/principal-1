import os, math
os.system("cls")

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
numero4 = float(input("Ingrese el cuarto número: "))
numero5 = float(input("Ingrese el quinto número: "))

numeros = [numero1, numero2, numero3, numero4, numero5]
numeros.sort(reverse=True)
tres_mayores = numeros[:3]
promedio = sum(tres_mayores) / 3

print("Los tres números mayores son:", tres_mayores)
print("El promedio de los tres números mayores es:", format(promedio, ".2f"))
