
varones = int(input("VARONES: "))
mujeres = int(input("MUJERES: "))

total = varones + mujeres

porcentaje_varones = int((varones * 100) / total)
porcentaje_mujeres = int((mujeres * 100) / total)

print("El porcentaje de varones es", porcentaje_varones, "%")
print("El porcentaje de mujeres es", porcentaje_mujeres, "%")