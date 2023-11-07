#Introducción a la Programación - sección: 17
#07/11/2023
#José Andrés Reyes Orellana
#Objetivo: Crear un programa capaz de ingresar datos relacionados a un Automovil
#Entrada: modelo, precio, marca, disponibilidad, TipoCambioDolar, descuentoAplicado
"""Proceso: 
1.Solicitar al usuario ingresar:
    modelo
    precio
    marca
    disponibilidad
    TipoCambioDolar
    descuentoAplicado
"""
"""Salida:
1. Se mostrara la informacion ingresada de manera ordenada
"""
class Automovil:
    def __init__(self, modelo = 0, precio = 0, marca = "", disponible = True, tipoCambioDolar = 0.0, descuentoAplicado = 0.0):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.disponible = disponible
        self.tipoCambioDolar = tipoCambioDolar
        self.descuentoAplicado = descuentoAplicado

def DefinirModelo(self, unmodelo):
    self.modelo = unmodelo

def Disponibilidad(self): 
    self.disponible = not self.disponible

def AplicarDescuento(self): 
    self.descuentoAplicado = miDescuento
    self.precio -= self.precio*(miDescuento/100)

def __str__(self):
    return f"Modelo: {self.modelo}\nprecio{self.precio}\nMarca{self.marca}\ndisponibilidad{self.disponible}\ntipo de cambio de dolar{self.tipoCambioDolar}\ndescuento{self.descuento}"

print("1. Ingrese la informacion")
print("2. Mostrar informacion")
print("3. Salir")

eleccion = input("Ingrese una opcion: ")

if eleccion == "1":
    unmodelo = int(input("Ingrese un modelo de Automovil: "))
    precio = float(input("Ingrese el precio del Automovil: "))
    marca = str(input("Ingrese la marca del Automovil: "))
    disponible = bool(input("Ingrese si el carro esta disponible: "))
    tipoCambioDolar = float(input("Ingrese el tipo de cambio al que se encuntra el dolar: "))
    descuentoAplicado = float(input("Ingrese el descuento que tiene el Automovil: "))
    
    if disponibilidad == "si":
        disponibilidad == True
        print("Disponible")
    else:
        disponibilidad == False
        print("No Disponible")
