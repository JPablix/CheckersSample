#Sample of a mini chekers with text interface

tablero = []

def crear_tablero():
    for i in range(8):
        tablero.append(["O"] * 8)

def imprimir_tablero(tablero):
    for fila in tablero:
        print("")
        for elemento in fila:
            print(elemento, end=" ")

crear_tablero()
imprimir_tablero(tablero)
