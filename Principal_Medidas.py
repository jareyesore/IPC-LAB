#Introduccion a la Programacion - seccion: 17
#10/10/2023
#Jose Andres Reyes Orellana
#Objetivo: Invocaral al módulo para conversión de una moneda a otra
#Entrada: cantidad de moneda
"""Proceso: 
1. Crear un módulo con las conversiones deseadas e importarlo
2. Solicitar al usuario una cantidad en cm
3. Solicitar al usuario elejir una operación
"""
"""Salida:
1. Obtención del resultado de la operación realizada
"""
try: 
    import Medidas
    cm= float(input("ingrese una distancia en cm: "))
    print("1. cm a m")
    print("2. cm a km")
    print("3. cm a pulg")
    print("4. cm a ft")
    print("5. Salida")
    while cm != 5:
        Eleccion = int(input("Seleccione la operación que desea realizar = "))
        if (Eleccion == 1):
            m=round(Medidas.centimetrosAmetros(cm),2)
            print(cm,"centimetros equivale a", m, "metros")
        elif (Eleccion == 2):
            km=round(Medidas.centimetrosAkilometros(cm),2)
            print(cm,"centimetros equivale a", km, "kilometros")
        elif (Eleccion == 3):
            pulg=round(Medidas.centimetrosApulgadas(cm),2)
            print(cm,"centimetros equivale a", pulg, "pulgadas")
        elif (Eleccion == 4):
            ft=round(Medidas.centimetrosApies(cm),2)
            print(cm,"centimetros equivale a", ft, "pies")
        else:
            break
except ValueError: 
    print("El valor ingresado no es un dato númerico, ingresar un número")