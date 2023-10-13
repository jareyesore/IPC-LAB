#Introduccion a la programacion, seccion 17
#21/09/2023
#José Andrés Reyes Orellana
#objetivo: Crear un programa que muestre la tabla de multiplicar de un número brindado por el usuario
#Entrada: numeros enteros entre el 1 y 10
"""Proceso:
1. solicitar al usuario un numero entre el 1 y el 10
2. Confirmar que el número este dentro del rango
"""
"""Salida:
1.tabla de multiplicar del numero ingresado dentro del rango
"""
print("José Andrés Reyes Orellana")
while True:
    try:
        n1=int(input("ingresar numero entre 1 y 10: "))
        if (n1<1 or n1>10):
            print("el numero ingresado no es valido")
        else:
            for i in range(1,11):
                resultado=(n1*i)
                print(n1, "*", i, "=", resultado)
    except ValueError:
        print("el valor ingresado no es un número")
    loop=input("desea ingresar otro valor? S/N: ")
    if loop.upper() !="S":
        break
SystemExit
