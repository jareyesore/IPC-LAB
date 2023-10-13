#Introduccion a la programacion, seccion 17
#28/09/2023
#José Andrés Reyes Orellana
#objetivo: Llegar a mostrar diferentes secuencias de números
#Entrada: Números de 1 a 25, 25 a 50 y de 20 a 0
"""Proceso:
1. Utilizar for para dar una secuencia de 1-25 que aumente de 1 en 1
2. Repetir usando While
3. repetir este proceso con las secuencias: 
    5-50 aumentando de 5 en 5
    20-0 decrementando de 2 en 2
"""
"""Salida:
1. Se mostrara la secuncia de número solicitado
"""
i = 1
print("uso de For de 1 a 25")
for i in range (1,26):
    print (i)
    i = i + 1
print ("uso de while de 1 a 25")
num1=1
while num1 <= 25:
    print(num1)
    num1 = num1 + 1
num2 = 5
print("uso de For de 5 a 50")
for num2 in range (5,51,5):
    print (num2)
    num2 = num2 + 5
print ("uso de while de 5 a 50")
num3 = 5
while num3 <= 50:
    print(num3)
    num3 = num3 + 5
num4 = 20
print("uso de For de 20 a 0")
for num4 in range (20,0,-2):
    print (num4)
    num4 = num4 - 2
print ("uso de while de 20 a 0")
num5 = 20
while num5 > 0:
    print(num5)
    num5 = num5 - 2