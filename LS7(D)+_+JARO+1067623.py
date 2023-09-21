#Introducción a la Programación - sección: 17
#19/09/2023
#José Andrés Reyes Orellana
#Objetivo: Crear un programa que permita al usuario ingresar datos y mostrar el resultado de diversas operaciones
#Entrada: a, b, c
"""Proceso: 
1. Solicitar al usuario asignar valores para a, b y c
2. Realizar las diversas operaciones
"""
"""Salida:
1. Mostrar en pantalla el resultado de diversas operaciones
""" 
import math
import os
While: True
print("ejercicio 3: ")
a = int(input("Ingrese un valor para la vaiable a = "))
b = int(input("Ingrese un valor para la vaiable b = "))
c = int(input("Ingrese un valor para la vaiable c = "))
print("1. a*b+c")
print("2. a*(b+c)")
print("3. a/b*c")
print("4. 3a+2b/c**2")
print("5. Ecuación cuadrática")
print("6. Salir")
Elección = int(input("Seleccione la operación que desea realizar = "))
while Elección != 6:
    Elección = int(input("Seleccione la operación que desea realizar = "))
    if Elección == 1:
        print(a, "*", b, "+", c, "=", a*b+c)
    elif Elección == 2:
        print(a, "* (", b, "+", c, ") =", a*(b+c))
    elif Elección == 3:
        print(a, "/", b, "*", c, "=", a/(b*c))
    elif Elección == 4:
        try:
            print("3 (", a, ") + 2 (", b, ") / ", c, "** 2 = ", ((3*a)+(2*b))/c**2)
        except ZeroDivisionError:
            print("No se puede dividir entre cero")
    elif Elección == 5:
        try:
            print("Ecuación Cuadrática")
            discriminante =  b**2 - 4 * a * c
            if discriminante < 0:
                print('La ecuación no tiene solución en el campo de los numeros reales.')
            else:    
                sol1 = (-b + math.sqrt(discriminante)) / (2 * a)
            if(discriminante != 0):
                sol2 = (-b - math.sqrt(discriminante)) / (2 * a)
                print("Solucion 1: ", sol1)
                print("Solucion 2: ", sol2)
            else:
                print("Solucion unica: ", sol1)
        except ZeroDivisionError:
            print("No se puede dividir entre cero")
    elif Elección == 6:
        break
    else:
        print("El valor ingresado no se encuentra dentro del rango definido")
