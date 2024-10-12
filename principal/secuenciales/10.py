import os
os.system("cls")

numero = int(input("Ingrese un número: "))

c1 = numero // 1000          
c2 = (numero % 1000) // 100 
c3 = (numero % 100) // 10    
c4 = numero % 10             

print("Cifra en la posición de miles:", c1)
print("Cifra en la posición de centenas:", c2)
print("Cifra en la posición de decenas:", c3)
print("Cifra en la posición de unidades:", c4)


print("Total de cifras:", len(str(numero)))