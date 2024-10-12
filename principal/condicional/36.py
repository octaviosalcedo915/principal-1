
import os
os.system("cls")

cant_cuadernos = int(input("Ingrese la cantidad de cuadernos: "))


if cant_cuadernos < 12:
    print("No se obsequia ningún lapicero.")
elif 12 <= cant_cuadernos < 24:
    lap_lucas = cant_cuadernos // 4
    print("De obsequio lleva:", lap_lucas, "Lapiceros Lucas.")
elif 24 <= cant_cuadernos < 36:
    lap_faber = (cant_cuadernos // 4) * 2
    print("De obsequio lleva:", lap_faber, "Lapiceros Faber.")
elif cant_cuadernos >= 36:
    lap_pilot = (cant_cuadernos // 4) * 2
    lap_faber = (cant_cuadernos // 6)
    lap_lucas = (cant_cuadernos // 12)
    
    print("De obsequio lleva:")
    print("Lapiceros Pilot:", lap_pilot)
    print("Lapiceros Faber:", lap_faber)
    print("Lapiceros Lucas:", lap_lucas)