#Introducción a la Programación - sección: 17
#12/09/2023
#José Andrés Reyes Orellana
#Objetivo: Crear un progrma que determine si un número es positivo, negativo o cero
#Entrada: Numero_1
"""Proceso: 
1. Solicitar al usuario ingresar un número
2. Determinar si el número es positivo, negativo o cero
"""
"""Salida:
1. Mostrar un mensaje que indique si el número es positivo, negativo o cero
2. Si el usario ingresa un texto, mostrar un mensaje
"""

try:

    print("Ejercicio 1")
    Numero_1 = int(input("Ingrese un número entero = "))
    if (Numero_1 < 0):
        print(Numero_1, "es un número negativo")
    elif (Numero_1 == 0):
        print(Numero_1, "es el número cero")
    else:
        print(Numero_1, "es un número positivo")

except ValueError: 
    print("El dato no es númerico, ingresar un número")