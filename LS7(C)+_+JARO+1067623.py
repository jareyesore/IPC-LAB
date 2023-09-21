#Introducción a la Programación - sección: 17
#19/09/2023
#José Andrés Reyes Orellana
#Objetivo: Crear un programa que permita al usuario ingresar datos y mostrar el resultado a diversas operaciones
#Entrada: a, b, c
"""Proceso: 
1. Solicitar al usuario asignar valores para a, b y c
2. Realizar diversas operaciones con los datos ingresados
"""
"""Salida:
1. Mostrar en pantalla el resultado de las operaciones realizadas
"""
print("ejercicio 3: Jerarquía de operaciones")
a = int(input("Ingrese un valor para la variable a = "))
b = int(input("Ingrese un valor para la variable b = "))
c = int(input("Ingrese un valor para la variable c = "))
print(a, "*", b, "+", c, "=", a*b+c)
print(a, "* (", b, "+", c, ") =", a*(b+c))
print(a, "/", b, "*", c, "=", a/(b*c))
print("3 (", a, ") + 2 (", b, ") / ", c, "** 2 = ", ((3*a)+(2*b))/c**2)