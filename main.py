def a_power_b(a, b):
    
    repetir = b
    potencia = 1

    for i in range(0,repetir):
        potencia = potencia * a
    
    return potencia

contador_errores = 0
contador_pares = 0
contador_impares = 0

#Este ciclo nos permite usar el try-except para intentar solucinar errores en la ejecución
while True: 

    #Si se introduce una base válida, el ciclo se rompe y se continúa con la línea 28
    try: 
        a = int(input("Ingrese un número entero que será la base de la potencia a realizar: "))
        break

    #Si no se introduce una base válida, se regresa el try.
    except ValueError:
        print("ERROR, ENTRADA NO VÁLIDA, INTENTELO DE NUEVO")
        contador_errores = contador_errores + 1
        

while a != 0:

    #Al igual que con la base, este ciclo permite solucionar los errores al solicitar el exponente
    while True: 
                
        #Si el exponente es un entero, el código se ejecuta normal
        try: 

            b = int(input("Ingrese un número entero que será el exponente al que se elevará la base {}: ".format(a)))

            potencia = a_power_b(a, b)

            if (potencia % 2 ==0):
                contador_pares = contador_pares + 1
            else:
                contador_impares = contador_impares + 1

            print("El resultado de elevar {} a la {} es: {}".format(a,b,potencia))

            #Indicación para hacer que el programa se detenga:
            print("SI YA NO DESEA CALCULAR MÁS POTENCIAS, CUANDO SE LE SOLICITE LA BASE, DIGITE 0")

            #Se solicita una nueva base.
            while True: 

                try:
                    a = int(input("Ingrese un número entero que será la base de la potencia a realizar: "))
                    break
                
                except (ValueError):
                    print("ERROR, ENTRADA NO VÁLIDA, INTENTE DE NUEVO")
                    contador_errores = contador_errores + 1


            #Si el usuario digita 0, el programa se detiene e imprime los contadores. 
            if a ==0:
                print("PROGRAMA FINALIZADO")
                print("La cantidad de veces que la potencia fue par es: {}".format(contador_pares))
                print("La cantidad de veces que la potencia fue impar es: {}".format(contador_impares))
                print("La cantidad de errores que ocurrieron fue: {}".format(contador_errores))

            break

        #Si el exponente no es válido, se solicita nuevamente
        except ValueError:
            print("ERROR, ENTRADA NO VÁLIDA, INTENTE DE NUEVO")
            contador_errores = contador_errores + 1







