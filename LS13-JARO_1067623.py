#Introduccion a la programacion, seccion 17
#31/10/2023
#José Andrés Reyes Orellana
#objetivo: Crear un programa capaz de devolver nombre. apellido. apellido de casada, nacimiento
#Entrada: nombre. apellido. apellido de casada, nacimiento
"""Proceso:
1. Crear una clase que almacene la información
"""
"""Salida:
1. Se mostraránm los datos ingresados
"""
import datetime
class información:
    def __init__(self):
        self.nombre = ""
        self.apellidos = ""
        self.apellidocasada = ""
        self.nacimineto = None
    
    def obtener_nombre(self):
        self.nombres = nombres
        
    def obtener_apellidos(self):
        self.apellido = apellidos
    
    def obtener_apellido_casada(self):
        self.apéllido_casada = apellidocasada

    def obtener_nacimiento(self):
        self.nacimiento = nacimiento
        if self.nacimiento: 
            hoy = datetime.date.today()
            edad = hoy.year - self.nacimiento.year - ((hoy.month, hoy.day) < (self.nacimiento.month, self.nacimiento.month))
        else: 
            return edad

persona = información()

nombres = input("Ingrese sus nombres: ")
apellidos = input("Ingrese sus apellidos: ")
apellidocasada = input("Ingrese apellido de casada: ")
nacimiento = input("Ingrese su fecha de nacimiento (dia/mes/año): ")