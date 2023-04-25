import random
from abc import ABC


class Character(ABC):
    def __init__(self):
        self.vida = 50
        self.posicion = None


class Alien(Character):
    def __init__(self):
        super().__init__()

    def move(self, direccion, tablero, casillas):
        fila, columna = self.posicion
        if direccion == "arriba":
            fila -= casillas
        elif direccion == "abajo":
            fila += casillas
        elif direccion == "izquierda":
            columna -= casillas
        elif direccion == "derecha":
            columna += casillas

        if columna < 0:
            return False

        if not tablero.obtener_celda(fila, columna):
            return False

        celda = tablero.obtener_celda(fila, columna).value
        if celda == "+":
            self.vida += 10
        elif celda == "-":
            self.vida -= 10
        elif celda == "#":
            return False
        elif isinstance(celda, Pedrator):
            self.vida -= 25
            # Ambos personajes quedan en la misma celda
            return True

        self.posicion = (fila, columna)
        return True

    def attack(self, predator):
        posicion_predator = predator.posicion
        if (self.posicion[0] == posicion_predator[0]) and ((posicion_predator[1] - self.posicion[1]) == 1 or
                                                           (posicion_predator[1] - self.posicion[1]) == -1):
            return True
        elif (self.posicion[1] == posicion_predator[1]) and ((posicion_predator[0] - self.posicion[0]) == 1 or
                                                             (posicion_predator[0] - self.posicion[0]) == -1):
            return True
        elif (self.posicion[0] - posicion_predator[0] == 1 and self.posicion[1] - posicion_predator[1] == 1) or \
                (self.posicion[0] - posicion_predator[0] == -1 and self.posicion[1] - posicion_predator[1] == -1) or \
                (self.posicion[0] - posicion_predator[0] == 1 and self.posicion[1] - posicion_predator[1] == -1) or \
                (self.posicion[0] - posicion_predator[0] == -1 and self.posicion[1] - posicion_predator[1] == 1):
            return True
        elif self.posicion == predator.posicion:
            return False
        else:
            return False


class Pedrator(Character):
    def __init__(self):
        super().__init__()

    def move(self, tablero):
        fila, columna = self.posicion
        direcciones_posibles = ["arriba", "abajo", "izquierda", "derecha"]
        casillas_a_moverse = [1, 2]
        direccion = random.choice(direcciones_posibles)
        if direccion == "arriba":
            fila -= random.choice(casillas_a_moverse)
        elif direccion == "abajo":
            fila += random.choice(casillas_a_moverse)
        elif direccion == "izquierda":
            columna -= random.choice(casillas_a_moverse)
        elif direccion == "derecha":
            columna += random.choice(casillas_a_moverse)

        if not tablero.obtener_celda(fila, columna):
            return False

        celda = tablero.obtener_celda(fila, columna).value
        if celda == "+":
            self.vida += 10
        elif celda == "-":
            self.vida -= 10
        elif celda == "#":
            return False

        if celda is not None:
            self.posicion = (fila, columna)
            return True
        else:
            return False



