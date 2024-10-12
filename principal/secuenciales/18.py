
import os
os.system("cls")

cant_producto = int(input("Ingrese la cantidad adquirida: "))
precio_producto = float(input("Ingrese el precio del artículo: "))

importe_compra = precio_producto * cant_producto

primer_descuento = importe_compra * 0.15
descuento1 = importe_compra - primer_descuento

segundo_descuento = descuento1 * 0.15
importe_a_pagar = descuento1 - segundo_descuento

print("El importe de la compra es S/.", format(importe_compra, ".2f"))
print("El primer descuento fue de S/.", format(primer_descuento, ".2f"))
print("El segundo descuento fue de S/.", format(segundo_descuento, ".2f"))
print("El importe a pagar es de S/.", format(importe_a_pagar, ".2f"))
