import random
from abc import ABC


class Character(ABC):
    def __init__(self):
        self.vida = 50
        self.posicion = None


class Alien(Character):
    def __init__(self):
        super().__init__()

    def move(self, direccion, tablero):
        fila, columna = self.posicion
        if direccion == "arriba":
            fila -= 1
        elif direccion == "abajo":
            fila += 1
        elif direccion == "izquierda":
            columna -= 1
        elif direccion == "derecha":
            columna += 1

        if not tablero.obtener_celda(fila, columna):
            return False

        celda = tablero.obtener_celda(fila, columna).value
        if celda == "+":
            self.vida += 10
        elif celda == "-":
            self.vida -= 10
        elif isinstance(celda, Pedrator):
            self.vida -= 25
            # Ambos personajes quedan en la misma celda
            return True

        self.posicion = (fila, columna)
        return True

    def attack(self):
        pass


class Pedrator(Character):
    def __init__(self):
        super().__init__()

    def move(self, tablero):
        fila, columna = self.posicion
        direcciones_posibles = ["arriba", "abajo", "izquierda", "derecha"]
        direccion = random.choice(direcciones_posibles)
        if direccion == "arriba":
            fila -= 1
        elif direccion == "abajo":
            fila += 1
        elif direccion == "izquierda":
            columna -= 1
        elif direccion == "derecha":
            columna += 1

        if not tablero.obtener_celda(fila, columna):
            return False

        celda = tablero.obtener_celda(fila, columna).value
        if celda == "+":
            self.vida += 10
        elif celda == "-":
            self.vida -= 10

        if celda is not None:
            self.posicion = (fila, columna)
            return True
        else:
            return False



