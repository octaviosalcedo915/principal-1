import os
os.system("cls")

numero = int(input("Ingrese un número de cuatro dígitos: "))

c1 = numero // 1000          
c2 = (numero % 1000) // 100  
c3 = (numero % 100) // 10    
c4 = numero % 10             

numero_reves = (c4 * 1000) + (c3 * 100) + (c2 * 10) + c1

print("El número al revés es:", numero_reves)