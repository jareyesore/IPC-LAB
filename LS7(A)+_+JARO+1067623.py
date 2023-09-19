#Introducción a la Programación - sección: 17
#19/09/2023
#José Andrés Reyes Orellana
#Objetivo: Crear un programa el cual utilize dos números los cuales realizen diversas operaciones aritméticas
#Entrada: Numero1, Numero2
"""Proceso: 
1. Solicitar al usurio ingresar dos valores numericos
2. Aplicar las operaciones de aritmética básica con los datos ingresados
"""
"""Salida:
1. Obtención del resultado de la operación realizada
2. Mostrar el resultado utilizando el formato deseado
""" 
print("ejercicio 1: operaciones aritméticas")
Numero1 = int(input("Ingrese el primer número = "))
Numero2 = int(input("Ingrese el segundo número = "))
print(Numero1, "+", Numero2, "=", Numero1+Numero2)
print(Numero1, "-", Numero2, "=", Numero1-Numero2)
print(Numero1, "*", Numero2, "=", Numero1*Numero2)
print(Numero1, "/", Numero2, "=", Numero1/Numero2)
print(Numero1, "%", Numero2, "=", Numero1%Numero2)
print(Numero1, "**", Numero2, "=", Numero1**Numero2)
print(Numero1, "//", Numero2, "=", Numero1//Numero2)