import os
os.system("cls")

gigabytes = int(input("Ingrese capacidad de disco en GB: "))

megabytes = gigabytes * 1024            
kilobytes = megabytes * 1024             
cbytes = kilobytes * 1024                 

print("La capacidad del disco duro es:", gigabytes, "GB")
print("En Megabytes es:", megabytes, "MB")
print("En Kilobytes es:", kilobytes, "KB")
print("En bytes es:", cbytes, "B")