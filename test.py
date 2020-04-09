#Un número es perfecto si sus divisores, exceptuando el mismo número, suman el mismo número.

def perfect_number (numero):

    #Determinar suma de divisores

    suma = 0

    for i in range (numero-1, 0, -1):
        if (numero % i == 0) :
            suma = suma + i 
        
    if suma == numero:
        print(("El número {} es perfecto").format(numero))
    else:
        print(("El número {} no es perfecto").format(numero))


numero = int(input("Ingrese un número entero para saber si es o no perfecto: "))

perfect_number(numero)