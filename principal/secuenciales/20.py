
import os
os.system("cls")

dinero = int(input("Ingrese la cantidad de dinero: S/. "))

billetes200 = dinero // 200
billetes100 = (dinero % 200) // 100
billetes50 = (dinero % 200) % 100 // 50
billetes20 = ((dinero % 200) % 100) % 50 // 20
billetes10 = (((dinero % 200) % 100) % 50) % 20 // 10
moneda5 = ((((dinero % 200) % 100) % 50) % 20) % 10 // 5
moneda2 = (((((dinero % 200) % 100) % 50) % 20) % 10) % 5 // 2
moneda1 = ((((((dinero % 200) % 100) % 50) % 20) % 10) % 5) % 2 // 1

print("BILLETES DE 200 SOLES: ", int(billetes200))
print("BILLETES DE 100 SOLES: ", int(billetes100))
print("BILLETES DE 50 SOLES: ", int(billetes50))
print("BILLETES DE 20 SOLES: ", int(billetes20))
print("BILLETES DE 10 SOLES: ", int(billetes10))
print("MONEDAS DE 5 SOLES: ", int(moneda5))
print("MONEDAS DE 2 SOLES: ", int(moneda2))
print("MONEDAS DE 1 SOL: ", int(moneda1))
