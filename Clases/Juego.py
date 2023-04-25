import random

from Clases.Character import Alien, Pedrator
from Clases.Tablero import Tablero


class Juego:
    def __init__(self, size):
        self.tablero = Tablero(size)
        self.celdas_vacias = self.obtener_celdas_vacias()
        self.alien = Alien()
        self.depredador = Pedrator()
        self.agregar_depredador()

    def obtener_celdas_vacias(self):
        celdas_vacias = []
        for fila in range(self.tablero.n):
            for columna in range(self.tablero.n):
                if self.tablero.obtener_celda(fila, columna).value is None:
                    celdas_vacias.append((fila, columna))
        return celdas_vacias

    def agregar_alien(self, fila, columna):
        if self.depredador.posicion == (fila, columna):
            print("El Alien no puede estar en la misma posición que el Depredador")
            return False
        elif self.tablero.obtener_celda(fila, columna).value is not None:
            print("La celda donde intenta agregar el Alien no está vacía")
            return False
        else:
            self.alien.posicion = (fila, columna)
            self.tablero.obtener_celda(fila, columna).value = "👽"
            return True

    def agregar_depredador(self):
        fila, columna = random.choice(self.celdas_vacias)
        self.depredador.posicion = (fila, columna)
        self.tablero.obtener_celda(fila, columna).value = "🤖"
        self.celdas_vacias.remove((fila, columna))

    def movimiento_alien(self):
        while True:
            direccion = input("Ingrese la direccion donde quiere mover el alien: ")
            numero_casillas = int(input("Ingrese el numero de casillas a moverse (1 o 2): "))
            if direccion in ["arriba", "abajo", "izquierda", "derecha"]:
                fila_anterior, columna_anterior = self.alien.posicion
                if self.alien.move(direccion, self.tablero, numero_casillas):
                    self.tablero.obtener_celda(fila_anterior, columna_anterior).value = None
                    self.tablero.obtener_celda(self.alien.posicion[0], self.alien.posicion[1]).value = "👽"
                    break
                else:
                    print("La celda a la que intenta moverse no existe")
            else:
                print("Dirección no válida")

    def movimiento_depredador(self):
        fila_anterior, columna_anterior = self.depredador.posicion
        self.tablero.obtener_celda(fila_anterior, columna_anterior).value = None
        self.depredador.move(self.tablero)
        if self.alien.posicion == self.depredador.posicion:
            self.alien.vida -= 25
        fila_anterior, columna_anterior = self.depredador.posicion
        self.tablero.obtener_celda(fila_anterior, columna_anterior).value = None
        self.tablero.obtener_celda(self.depredador.posicion[0], self.depredador.posicion[1]).value = "🤖"

    def juego_terminado(self):
        if self.alien.vida <= 0 or self.depredador.vida <= 0:
            return True

    def jugar(self):
        print("Tablero:")
        self.tablero.imprimir_tablero()
        while True:
            fila = int(input("Ingrese la fila donde comenzara el alien: "))
            columna = int(input("Ingrese la columna donde comenzara el alien: "))
            if self.agregar_alien(fila, columna):
                break
        while True:
            # Imprime el tablero
            print("Tablero:")
            self.tablero.imprimir_tablero()
            print(f"Vida del alien: {self.alien.vida}")
            print(f"Vida del depredador: {self.depredador.vida}")

            # Movimiento del Alien
            print("Turno del Alien")
            opcion = input("Moverse o atacar: ")
            if opcion == "moverse":
                self.movimiento_alien()
            if opcion == "atacar":
                if self.alien.attack(self.depredador):
                    self.depredador.vida -= 10
                else:
                    print("No se pudo realizar el ataque")
            else:
                print("Seleccione una opción correcta")

            # Movimiento del Depredador
            print("Turno del Depredador")
            self.movimiento_depredador()

            # Comprueba si el juego ha terminado
            if self.juego_terminado():
                print("El juego ha terminado")
                break


game = Juego(4)
game.jugar()




