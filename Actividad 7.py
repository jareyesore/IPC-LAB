#Introduccion a la programacion, seccion 17
#19/10/2023
#José Andrés Reyes Orellana
#objetivo: Crear un programa que le solicita al usuario una palabra y que muestre sus primeras tres letras
#Entrada: palabra brindada por el usuario
"""Proceso:
1. Solicitar una palabra al usuario
2. Indicar que unicamente se tomen sus 3 primeras letras
3. Solicitar al usuario una segunda palabra
4. Sustituir todas las "o" de la palabra por "x"
"""
"""Salida:
1. Se mostrán unicamente las 3 primeras letras de la palabra
2. Se mostrara la palabra modificada
"""
palabra = str(input("Ingrese una palabra: "))
leerletras = ""

for i in range(3):
    if i < len(palabra):
        letra = palabra[i]
        print(f"Letra {i + 1}: {letra}")
        leerletras += letra

print("Las primeres 3 letras de la palabra ingresada son:", leerletras)
input("Presione enter para continuar")

palabra2 = str(input("Ingrese una palabra: "))
textoalterado = ""

for letra in palabra2:
    if letra == "o":
        textoalterado +- "x"
    else:
        textoalterado +- letra

print ("La nueva palabra es:", textoalterado)

"""Situaciones en la que es util este tipo de función
1. Validar la entrada de un usuario.
2. Procesar y corregir texto que se encuntren mal escritos.
3. Sustituir palabras presentes en un texto. 
"""