import os
os.system("cls")


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

num1_c1 = num1 // 100          
num1_c2 = (num1 % 100) // 10    
num1_c3 = num1 % 10             

num2_c1 = num2 // 100          
num2_c2 = (num2 % 100) // 10    
num2_c3 = num2 % 10             

print("--- Números Intercambiados ---")
print("Primer Número: ", (num2_c3 * 100) + (num1_c2 * 10) + (num2_c1))
print("Segundo Número: ", (num1_c3 * 100) + (num2_c2 * 10) + (num1_c1))