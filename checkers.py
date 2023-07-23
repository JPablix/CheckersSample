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

    print("MENU \n 1. Iniciar juego \n 2. Cambio de nombres \n 3. Reglas del juego \n 4. Salir del juego")
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
    
####################
#Funciones del menu#
####################

def menu_opcion1():
    print("")
def menu_opcion2():
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



crear_tablero()
iniciar_fichas(tablero)

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