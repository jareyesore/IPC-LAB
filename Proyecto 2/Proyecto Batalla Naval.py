#Introducción a la Programación - sección: 17
#14/11/2023
#José Andrés Reyes Orellana
#Objetivo: Crear un programa capaz de recrear el juego de batalla naval
#Entrada: Barcos, Coordenadas, disparos
"""Proceso: 
1. Solicitar al jugador 1 colocar sus barcos en el tablero.
2. Solicitar al jugador 2 colocar sus barcos en el tablero.
3. Solicitar al jugador 1 ingresar una coordenada para realizar un disparo.
4. Solicitar al jugador 2 ingresar una coordenada para realizar un disparo.
"""
"""Salida:
1. Se mostrará un mensaje indicando si el impacto dio en un barco o fallo.
2. Se mostrará un mensaje de ganador cuando un jugador pierda todos sus barcos.
"""

#Crear el tablero de juego
def obtener_tablero():
    tablero = []
    for i in range (10):
        Filas = []
        for j in range(10):
            Filas.append(" ")
        tablero.append(Filas)

#Nombrar columnas
    Columnas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    print("   " + " ".join(Columnas))
    for num_fila, fila in enumerate(tablero, start=1):
        print(str(num_fila) + " " + "  ".join(fila))  
    return tablero  

#Colocar los barcos de los jugadores
def colocar_barcos(tablero, tamano, cantidad, num_jugador):
    for i in range(cantidad):
        print(f"Se esta colocando el barco de tamaño {tamano}. Barco {i + 1}/{cantidad}:")
        barco_colocado = False
        while not barco_colocado:
            try:
                #Solicitar al usuario las coordenadas para poner los barcos
                coordenada = input(f"Ingrese la coordenada donde se colocara el barco {i + 1} (Ejemplo: A1): ").upper()
                if len(coordenada) < 2 or not ("A" <= coordenada[0] <= "J") or not ("1" <= coordenada[1] <= "9"):
                    print("La coordenada ingresada no es valida. Ingresar correctamente la coordenada deseada.")
                    continue
                
                fila = int(coordenada[1:])
                columna = coordenada[0]
                orientacion = input(str("Ingrese la orientación del barco (vertical/horizontal): ")).lower()

                columna_index = ord(columna) - 65

                #Colocar los barcos de manera vertical
                if orientacion == "vertical":
                    if fila + tamano - 1 > 10:
                        print("El barco se encuntra fuera de los limites del juego. Intentalo de nuevo.")
                        continue
                    for j in range(tamano):
                        if tablero[fila - 1 + j][columna_index] != " ":
                            print("El barco se encuentra sobre otro barco. Intentalo de nuevo.")
                            break
                    else:
                        for j in range(tamano):
                            tablero[fila - 1 + j][columna_index] = "B"
                        mostrar_tablero_jugador(tablero, num_jugador)
                        barco_colocado = True
                
                #Colocar los barcos de manera horizontal
                elif orientacion == "horizontal":
                    if columna_index + tamano > 10:
                        print("El barco se encuntra fuera de los limites del juego. Intentalo de nuevo.")
                        continue
                    for j in range(tamano):
                        if tablero[fila - 1][columna_index + j] != " ":
                            print("El barco se encuentra sobre otro barco. Intentalo de nuevo.")
                            break
                    else: 
                        for j in range(tamano):
                            tablero[fila - 1][columna_index + j] = "B"
                        mostrar_tablero_jugador(tablero, num_jugador)
                        barco_colocado = True
                else:
                    print("La orientación no es valida. Intentalo de nuevo.")
            
            except (ValueError, IndexError):
                print("La entrada no es valida. Intentalo de nuevo.")
    
    #Mensaje despues de colocar todos los barcos en el tablero
    print("Los barcos fueron colocados exitosamente.")

#mostrar los tablero de los jugadores
def mostrar_tablero_jugador(tablero, jugador):
    print(f"Tablero J{jugador}: ")
    print("   " + " ".join(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]))
    for num_fila, fila in enumerate(tablero, start=1):
        if num_fila != 10:
            print(str(num_fila) + "  " + " ".join(fila))
        else:
            print(str(num_fila) + " " + " ".join(fila))

def mostrar_tablero_enemigo(tablero,jugador):
    print(f"Tablero J{jugador}: ")
    print("   " + " ".join(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]))
    for num_fila, fila in enumerate(tablero, start=1):
        fila_visible = [c if c in {"X", "-"} else " " for c in fila]
        if num_fila != 10:
            print(str(num_fila) + "  " + " ".join(fila_visible))
        else:
            print(str(num_fila) + " " + " ".join(fila_visible))

#Crear sistema de disparos
def disparar(tablero_oponente, fila, columna, jugador):

    if fila < 1 or fila > 10 or not ("A" <= columna <= "J"):
        print("Disparo fuera de los limites.")
        return
    
    columna_index = ord(columna) - 65
    
    if tablero_oponente[fila - 1][columna_index] == 'B':
        print("Le diste a un Barco!")
        tablero_oponente[fila - 1][columna_index] = 'X'
    elif tablero_oponente[fila - 1][columna_index] == ' ':
        print("No le diste a ningun barco.")
        tablero_oponente[fila - 1][columna_index] = '-'
    else: 
        print("Ya has disparado aquí antes.")
    
    print("Tablero del oponente actualizado: ")
    mostrar_tablero_enemigo(tablero_oponente, jugador)

def sistema_de_turnos():
    print("Bienvenidos a Batalla Naval")

    #Crear tablero de los jugadores
    tablero_jugador1 = obtener_tablero()
    tablero_jugador2 = obtener_tablero()

    #Colocar los barcos de los jugadores
    colocar_barcos(tablero_jugador1, 5, 2, 1)
    colocar_barcos(tablero_jugador1, 3, 3, 1)

    colocar_barcos(tablero_jugador2, 5, 2, 2)
    colocar_barcos(tablero_jugador2, 3, 3, 2)

    #Iniciar la secuencia de juego
    jugador_actual = 1
    jugadores = {1: ("Jugador 1", tablero_jugador1), 2: ("Jugador 2", tablero_jugador2)}

    while True:
        print(f"Es el turno de {jugadores[jugador_actual][0]}")
        print("Este es tu tablero:")
        mostrar_tablero_jugador(jugadores[jugador_actual][1],jugador_actual)
        print("Este es el tablero del oponente: ")
        mostrar_tablero_enemigo(jugadores[3 - jugador_actual][1],jugador_actual)

        while True:
            try:
                fila = int(input("Ingresa la fila en la que quieres realizar el disparo: "))
                columna = str(input("Ingresa la columna en la que desea el disparo: "))
                disparar(jugadores[3 - jugador_actual][1], fila, columna, jugador_actual)
                break
            except (ValueError):
                print("La entrada ingresada no es valida. Intentalo de nuevo. ")

         # Indicar cuando un jugador gane la partida
        if all('B' not in fila for fila in jugadores[3 - jugador_actual][1]):
            print(f"{jugadores[jugador_actual][0]} ha ganado la partida. ¡Felicidades!")
            break
        
        # ALternar al siguiente jugador
        jugador_actual = 3 - jugador_actual

# Ejecutar el sistema de turnos
sistema_de_turnos()