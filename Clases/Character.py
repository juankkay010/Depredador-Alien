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

        celda = tablero.obtener_celda(fila, columna)
        if celda == "+":
            self.vida += 10
        elif celda == "-":
            self.vida -= 10

        if celda is not None:
            self.posicion = (fila, columna)

    def attack(self):
        pass


class Pedrator(Character):
    def __init__(self):
        super().__init__()

    def move(self):
        pass

