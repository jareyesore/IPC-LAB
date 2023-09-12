#Introducción a la Programación - sección: 17
#12/09/2023
#José Andrés Reyes Orellana
#Objetivo: Crear un programa que indique el día de la semana
#Entrada: Numero_1
"""Proceso: 
1. Solicitar al usuario el día de la semana (1 a 7)
2. Determinar el día de la semana
"""
"""Salida:
1. Se indicara el día de la semana con un sistema númerico
2. Si el número esta fuera del rango, mostrar un mensaje
3. Si el usuario ingresa texto, mostrar un mensaje
"""

try:

    print("Ejercicio 2")
    Numero_1 = int(input("Ingrese el día de la semana (1 a 7) = "))
    if (Numero_1 == 1):
        print("El día de hoy es Lunes")
    elif (Numero_1 == 2):
        print("El día de hoy es Martes")
    elif (Numero_1 == 3):
        print("El día de hoy es Miercoles")
    elif (Numero_1 == 4):
        print("El día de hoy es Jueves")
    elif (Numero_1 == 5):
        print("El día de hoy es Viernes")
    elif (Numero_1 == 6):
        print("El día de hoy es Sabado")
    elif (Numero_1 == 7):
        print("El día de hoy es Domingo")
    else:
        print("El número esta fuera del rango establecido")

except ValueError: 
    print("El dato no es númerico, ingresar un número")