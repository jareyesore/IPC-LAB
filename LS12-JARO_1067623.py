#Introduccion a la programacion, seccion 17
#26/10/2023
#José Andrés Reyes Orellana
#objetivo: Crear un programa con la capacidad de administrar una lista de contactos
#Entrada: Contactos del usuario
"""Proceso:
1. Solicitar al usuario cuantos contactos ingresara
2. Ingresar Nombre y numero de telefono
3. Solicitar eliminar un contacto
4. Agregar un contacto en una posición específica
5. Ordenar alfabeticamente los contactos tanto ascendente como descendientes
"""
"""Salida:
1. Lista de contactos completa
2. Mostrar la lista según los datos ejecutados
"""
Listadecontactos = []
n = int(input("Ingrese la cantidad de contactos que desea ingresar: "))

for i in range (n):
    Nombre = str(input("Ingrese el nombre del contacto: "))
    Numero = int(input("Ingrese el número de teléfono del contacto: "))
    Contacto = [Nombre, Numero]
    Listadecontactos.append(Contacto)

print("Lista de contactos completa:")
for contacto in Listadecontactos:
    print(contacto)

eliminar = str(input("Ingrese el nombre del contacto que desea eliminar: "))
for contacto in Listadecontactos:
    if contacto[0] == eliminar:
        Listadecontactos.remove(contacto)
        break

print("Lista de contactos actualizada:")
for contacto in Listadecontactos:
    print(contacto)

Listadecontactos.sort()

nombre_nuevo = str(input("Ingrese el nombre del nuevo contacto: "))
numero_nuevo = int(input("Ingrese el número de teléfono del nuevo contacto: "))
nuevo_contacto = [nombre_nuevo.upper(), numero_nuevo]
Listadecontactos.append(nuevo_contacto)

print("Lista de contactos ordenada alfabéticamente:")
for contacto in Listadecontactos:
    print(contacto)

posicion = int(input("Ingrese la posición donde desea agregar un nuevo contacto: "))
nombre_nuevo = str(input("Ingrese el nombre del nuevo contacto: "))
numero_nuevo = int(input("Ingrese el número de teléfono del nuevo contacto: "))
nuevo_contacto = [nombre_nuevo, numero_nuevo]
Listadecontactos.insert(posicion, nuevo_contacto)

print("Lista de contactos completa:")
for contacto in Listadecontactos:
    print(contacto)

lista2 = Listadecontactos[:]
lista2.sort(reverse=True)

print("Lista ordenada de forma descendente:")
for contacto in lista2:
    print(contacto)

print("Lista original:")
for contacto in Listadecontactos:
    print(contacto)