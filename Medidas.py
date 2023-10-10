#Introduccion a la Programacion - seccion: 17
#10/10/2023
#Jose Andres Reyes Orellana
#Objetivo: Crear funciones para convertir de una medida a otra
#Entrada: cantidad de medida
"""Proceso: 
1. Definir la cantidad de medida
"""
"""Salida:
1. Definición de diversas conversiones
"""
#Convertir cm a m
def centimetrosAmetros(centimetros):
    total=centimetros/100
    return total

#Convertir cm a km
def centimetrosAkilometros(centimetros):
    total=centimetros/100000
    return total

#Convertir cm a pulg
def centimetrosApulgadas(centimetros):
    total=centimetros*0.393701
    return total

#Convertir cm a ft
def centimetrosApies(centimetros):
    total=centimetros*0.0328084
    return total