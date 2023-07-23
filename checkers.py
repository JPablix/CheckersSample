#Sample of a mini checkers with text interface

#Apuntes: Fichas blancas: W, fichas negras: B, casillas vacias: O, reinas blancas: Q, reinas negras: K
#         

####################
#Variables globales#
####################
tablero = []
jugador1 = "Jugador1"
jugador2 = "Jugador2"
juego_iniciado = True

#######################
#Funciones principales#
#######################
def crear_tablero():
    i = 0       
    while i <= 7:           #Creación de filas
        tablero.append([])
        j = 0

        if i%2 == 0:        #Saber con qué elemento empezar
            espacio = "O"
        else:
            espacio = "X"

        while j <= 7:       #Creación de columnas
            tablero[i].append(espacio)
            if espacio == "O":
                espacio = "X"
            else:
                espacio = "O"
            j += 1
        i += 1

def imprimir_tablero(tablero):
    for fila in tablero:
        print("")
        for elemento in fila:
            print(elemento, end=" ")
            
def iniciar_fichas(tablero):
    i = 0
    while i <= 2: #Se atraviesan las primeras 3 filas, i va a equivaler al numero de fila
        j = 0
        while j <= 7: #Se atraviesan las TODAS las columnas en la fila
            if tablero[i][j] == "O":
                tablero[i][j] = "W"
            j += 1
        i += 1
    
    i = 5
    while i <= 7:
        j = 0
        while j <= 7:
            if tablero[i][j] == "O":
                tablero[i][j] = "B"
            j += 1
        i += 1

def menu():
    print("\n---MENU--- \n 1. Iniciar juego \n 2. Cambio de nombres \n 3. Reglas del juego \n 4. Salir del juego")
    menu_opcion = input("Ingrese el numero de la opcion a la que desea ingresar: ")
    
    if menu_opcion == "1":
        menu_opcion1()
    elif menu_opcion == "2":
        menu_opcion2()
    elif menu_opcion == "3":
        menu_opcion3()
    elif menu_opcion == "4":
        if menu_opcion4() == True:
            return False
    else:
        print("Ingrese una opcion valida")
    return True

def imprimir_jugadores():
    print("Jugador 1: ", jugador1, "\t" "Jugador 2: ", jugador2)
####################
#Funciones del menu#
####################

def menu_opcion1():
    print("\n---INICIAR JUEGO---")
    crear_tablero()
    iniciar_fichas(tablero)

    turno = 1   #turno = 1 -> jugador1, turno = 2 -> jugador2

    while True:

        imprimir_jugadores()

        if turno == 1:
            print("\nTurno de: ", jugador1)
        else:
            print("\nTurno de: ", jugador2)
        imprimir_tablero(tablero)

        continuar = input("\nPresione ENTER para continuar o M para volver al menu: ")
        if continuar == "M" or continuar == "m":
            break
        
        #Verificar que la posición sea válida
        posicion_valida = False
        while not posicion_valida:
            fila_ficha = int(input("Ingrese la fila de la ficha que desea mover: "))
            columna_ficha = int(input("\nIngrese la columna de la ficha que desea mover: "))
            if fila_ficha <= 7 and fila_ficha >= 0 and columna_ficha <= 7 and columna_ficha >= 0:
                posicion_valida = True
            else:
                print("Posición no válida")

        #Movimiento de fichas blancas
        if turno == 1:
            #Verificamos que haya una ficha
            movimiento_blancas = True
            while movimiento_blancas:
                if tablero[fila_ficha][columna_ficha] == "W" or tablero[fila_ficha][columna_ficha] == "Q":
                    #Verificamos que tipo de ficha tenemos

                    #Ficha normal
                    if tablero[fila_ficha][columna_ficha] == "W":
                        #Verificamos que el movimiento sea válido
                        movimiento_valido = False
                        while not movimiento_valido:
                            fila_destino = int(input("Ingrese la fila a la que desea mover la ficha: "))
                            columna_destino = int(input("\nIngrese la columna a la que desea mover la ficha: "))
                            if fila_destino <= 7 and fila_destino >= 0 and columna_destino <= 7 and columna_destino >= 0:
                                #Movimiento normal hacia abajo
                                if fila_destino == fila_ficha + 1 and columna_destino == columna_ficha -1:
                                    movimiento_valido = True
                                elif fila_destino == fila_ficha + 1 and columna_destino == columna_ficha + 1:
                                    movimiento_valido = True
                                else:
                                    print("Movimiento no válido")
                                if tablero[fila_destino][columna_destino] != "O":
                                    movimiento_valido = False
                        
                        #Removemos la ficha de su posición original
                        tablero[fila_ficha][columna_ficha] = "O"
                        #Colocamos la ficha en su nueva posición
                        tablero[fila_destino][columna_destino] = "W"
                    #Detener la petición de movimiento de fichas blancas
                    turno = 2
                    break     
                elif tablero[fila_ficha][columna_ficha] == "O" or tablero[fila_ficha][columna_ficha] == "X":
                    print("No hay una ficha en esa posición")
                elif tablero[fila_ficha][columna_ficha] == "B" or tablero[fila_ficha][columna_ficha] == "K":
                    print("Esa ficha no es tuya")
        #Movimiento de fichas negras
        else:
            print("")
            
        
        #Mini TO DO:
        #Mover ficha
        #Validar que ficha se va a mover                            X
            #Posición de la ficha a mover (fila,columna) sea válida X
            #Posición de la ficha a mover (fila,columna)            X
            #Verificar que haya una ficha                           X
            #Verificar que la ficha sea del jugador que le toca     X
        #Validar que movimiento se va a hacer
            #Verificar que si la ficha es NORMAL solo se mueva hacia adelante           X
            #Verificar que si la ficha es REINA se mueva hacia adelante y hacia atrás   

            #Posición a la que se va a mover (fila,columna)                             X
            #Verificar que la posición esté vacía                                       X
            #Verificar que la posición esté dentro del tablero                          X

            #Verificar la acción de comer


def menu_opcion2():
    print("\n---CAMBIO DE NOMBRES---")
    global jugador1
    global jugador2

    jugador1 = input("Ingrese el nombre para el jugador #1: ")
    jugador2 = input("Ingrese el nombre para el jugador #2: ")

def menu_opcion3():
    print("\n---REGLAS DEL JUEGO---")
    print("Tablero: El juego se juega en un tablero de 8x8 casillas, similar al tablero de ajedrez.\n\nPiezas: Cada jugador tiene 12 piezas, que se colocan en las 12 casillas más cercanas a ellos en las tres filas más cercanas.\n\nMovimiento: Las piezas solo se pueden mover en diagonal, una casilla a la vez, hacia adelante en el tablero (hacia la fila del oponente). Las piezas blancas (o rojas, dependiendo de la variante regional) se mueven hacia arriba, mientras que las piezas negras (o negras) se mueven hacia abajo.\n\nCaptura: Si una pieza rival está diagonalmente adyacente y hay una casilla vacía inmediatamente más allá de esa pieza, puedes capturarla saltando sobre ella hacia la casilla vacía. La pieza capturada se retira del tablero. Si hay otras capturas posibles desde la nueva posición de la pieza, puedes continuar saltando sobre las piezas enemigas en una secuencia de captura múltiple.\n\nCoronación: Cuando una pieza alcanza la última fila del lado opuesto del tablero, la fila más alejada de su posición inicial, se corona y se convierte en dama. La dama puede moverse hacia adelante y hacia atrás en diagonal, lo que amplía su rango de movimiento y hace que sea más poderosa.\n\nMovimiento de la dama: Las damas pueden moverse en diagonal hacia adelante o hacia atrás en cualquier distancia, siempre y cuando haya casillas vacías en su ruta. Al igual que las piezas normales, las damas pueden capturar saltando sobre una pieza enemiga diagonalmente adyacente, y también pueden realizar capturas múltiples si es posible.\n\nObjetivo: El objetivo del juego es capturar todas las piezas del oponente o bloquearlas para que no puedan moverse.")
    
    while True:
        volver_menu = input("Presione M para volver al menu: ")
        if volver_menu == "M" or volver_menu == "m":
            menu()
        else:
            print("Ingrese una opcion correcta")

def menu_opcion4(): 
    print("\n---SALIR DEL JUEGO---")
    while True:
        salir = input("¿Estás seguro que deseas salir del juego? (Y/N): ")
        if salir == "Y" or salir == "y":
            print("Gracias por jugar")
            return True
        elif salir == "N" or salir == "n":
            return False
        else:
            print("Ingrese una opcion correcta")
            
        

####################
#Programa Principal#
####################

while juego_iniciado:
    juego_iniciado = menu()




#TO DO:
    #Cuando se corre el juego lo primero que hay que hacer es crear el tablero e iniciar las fichas
    #Luego se debe desplegar un menú con las siguientes opciones:
        #1. Iniciar un juego nuevo (Desplegar el tablero y el turno del jugador)
        #2. Cambiar los nombres de los jugadores (por defecto son Jugador1 y Jugador2)(Al ingresar en esta opción se piden dos nombres de jugadores)
        #3. Ver las reglas del juego    (Copiar y pegar las reglas del juego de internet)
        #4. Salir del juego (Termina la ejecución del juego)

        #NOTA: Se puede volver al menú en cualquier momento del juego si se presiona la tecla "M" y luego enter
        
    #Una vez se inicia el juego, se debe desplegar el tablero y el turno del jugador



#READY:
#W donde haya O en las primeras 3 líneas
#B donde haya O en las últimas 3 líneas 
#2 ciclos (for, while)
#Columna vertical, fila horizontal