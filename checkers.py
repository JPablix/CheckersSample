#Sample of a mini checkers with text interface

#Apuntes: Fichas blancas: W, fichas negras: B, casillas vacias: O, reinas blancas: Q, reinas negras: K
#         

tablero = []

def crear_tablero():
    i = 0       
    while i <= 8:           #Creación de filas
        tablero.append([])
        j = 0

        if i%2 == 0:        #Saber con qué elemento empezar
            espacio = "O"
        else:
            espacio = "X"

        while j <= 8:       #Creación de columnas
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


crear_tablero()
imprimir_tablero(tablero)

#W donde haya O en las primeras 3 líneas
#B donde haya O en las últimas 3 líneas 
#2 ciclos (for, while)