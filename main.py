def a_power_b(a, b):
    
    repetir = b
    potencia = 1

    for i in range(0,repetir):
        potencia = potencia * a
    
    return potencia


a = int(input("Ingrese la base de la potencia a realizar: "))

while a != 0:
    b = int(input("Ingrese el exponente al que desea elebar la base {}: ".format(a)))

    potencia = a_power_b(a, b)

    print("El resultado de elevar {} a la {} es: {}".format(a,b,potencia))

    #Indicación para hacer que el programa se detenga:
    print("SI YA NO DESEA CALCULAR MÁS POTENCIAS, CUANDO SE LE SOLICITE LA BASE, DIGITE 0")

    a = int(input("Ingrese la base de la potencia a realizar: "))

    if a ==0:
        print("PROGRAMA FINALIZADO")

    






