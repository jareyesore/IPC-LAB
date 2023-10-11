#Introduccion a la Programacion - seccion: 17
#27/09/2023
#Jose Andres Reyes Orellana
#Objetivo: Crear un programa capaz de mostrar un calculo factorial y una secuencia de Fibonacci
#Entrada: numero
"""Proceso: 
1. Desplegar un menu
2. Solicitar al usuario seleccionar una opción
3. Solicitar al usuario ingresar un número
"""
"""Salida:
1. Se mostrara el resultado deseado
2. Se dará la posibilidad de realizar otra operación
"""
#definimos la operación factorial
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero*factorial(numero-1)

#definimos la secuencia de Fibonacci
def fibonacci(numero):
    if numero <= 0:
        return []
    elif numero == 1:
        return [0]
    elif numero == 2:
        return [1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, numero):
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)
        return fib_sequence

try:
#Iniciamos el ciclo con la función While
    while True:
#Imprimimos el menú de acciones
        print ("Menú:")
        print ("1. Factorial")
        print ("2. Secuencia de Fibonacci")
        print ("3. Salir")
        Eleccion = int(input("Ingrese la acción que desee realizar: "))
#Especificamos que pasará en caso de seleccionar la opción 1
        if Eleccion == 1: 
            numero = int(input("De cual número desea la factorial: "))
            resultado = factorial(numero)
            print(numero, "! =", resultado)
#Especificamos que pasará en caso de seleccionar la opción 2
        elif Eleccion == 2:
            numero = int(input("De que numero quisiera conocer la Secuencia de Fibonacci: "))
            resultado = fibonacci(numero)
            print(",".join(map(str, resultado)), "... Fibonacci", numero)
#Especificamos que pasará en caso de seleccioanr la opción 3
        elif Eleccion == 3:
            break
        else:
            print("El número se encuntra fuera del rango, por favor seleccionar una opción valida")
#Instrucción para volver a iniciar el ciclo
        input("Presione enter para una nueva operación")