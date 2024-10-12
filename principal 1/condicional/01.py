import os
os.system("cls")

unidades = int(input("Ingrese la cantidad de unidades: "))

if 1 <= unidades <= 25:
    precio_unitario = 27
elif 26 <= unidades <= 50:
    precio_unitario = 25
else:  
    precio_unitario = 23
importe_compra = precio_unitario * unidades
if unidades > 50:
    descuento = importe_compra * 0.15  
else:
    descuento = importe_compra * 0.05   

total_a_pagar = importe_compra - descuento

print(f"Importe de la compra: S/. {importe_compra:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {total_a_pagar:.2f}")