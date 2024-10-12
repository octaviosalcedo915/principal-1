

def calcular_hipotenusa(cateto_a, cateto_b):
    """Calcula la hipotenusa de un triángulo rectángulo dado sus catetos."""
    hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
    return hipotenusa

def main():
    print("Cálculo de la Hipotenusa")
    
   
    try:
        cateto_a = float(input("Ingrese el valor del primer cateto (a): "))
        cateto_b = float(input("Ingrese el valor del segundo cateto (b): "))
        
        6
        resultado = calcular_hipotenusa(cateto_a, cateto_b)
        
        
        print(f"La hipotenusa del triángulo es: {resultado:.2f}")
    
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()