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
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Módulo")
print("6. Exponente")
print("7. Cociente")
print("8. Salir")
Elección = int(input("Seleccione la operación que desea realizar = "))
while Elección != 8:
    Elección = int(input("Seleccione la operación que desea realizar = "))
    if (Elección == 1):
        print(Numero1, "+", Numero2, "=", Numero1+Numero2)
    elif (Elección == 2):
        print(Numero1, "-", Numero2, "=", Numero1-Numero2)
    elif (Elección == 3):
        print(Numero1, "*", Numero2, "=", Numero1*Numero2)
    elif (Elección == 4):
        print(Numero1, "/", Numero2, "=", Numero1/Numero2)
    elif (Elección == 5):
        print(Numero1, "%", Numero2, "=", Numero1%Numero2)
    elif (Elección == 6):
        print(Numero1, "**", Numero2, "=", Numero1**Numero2)
    elif (Elección == 7):
        print(Numero1, "//", Numero2, "=", Numero1//Numero2)
    else:
        break