def a_power_b(a, b):
    
    repeticiones = b
    potencia = 1

    for i in range(0,repeticiones):
        potencia = potencia * a
    
    return potencia



a = int(input("Ingrese la base de la potencia a realizar: "))
b = int(input("Ingrese el exponente al que desea elebar la base {}: ".format(a)))

potencia = a_power_b(a, b)

print("El resultado de elevar {} a la {} es: {}".format(a,b,potencia))



