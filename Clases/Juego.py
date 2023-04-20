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
        self.alien.posicion = (fila, columna)
        self.tablero.obtener_celda(fila, columna).value = "A"

    def agregar_depredador(self):
        fila, columna = random.choice(self.celdas_vacias)
        self.depredador.posicion = (fila, columna)
        self.tablero.obtener_celda(fila, columna).value = "D"
        self.celdas_vacias.remove((fila, columna))







