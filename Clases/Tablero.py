from Clases.Character import Alien
from Clases.LinkedList import LinkedList
import random


class Tablero:
    def __init__(self, n):
        self.n = n
        self.tablero = LinkedList()
        self.crear_tablero()
        self.agregar_simbolos()

    def crear_tablero(self):
        for i in range(self.n):
            row = LinkedList()
            for j in range(self.n):
                row.add_at_tail(None)
            self.tablero.add_at_tail(row)

    def obtener_celda(self, fila, columna):
        if fila >= self.n or columna >= self.n:
            return False
        current_fila = self.tablero.head
        for i in range(fila):
            current_fila = current_fila.next
        current_celda = current_fila.value.head
        for i in range(columna):
            current_celda = current_celda.next
        return current_celda

    def imprimir_tablero(self):
        fila_actual = self.tablero.head
        while fila_actual:
            nodo = fila_actual.value.head
            fila = " "
            while nodo:
                if nodo.value is None:
                    fila += "o"
                else:
                    fila += nodo.value
                nodo = nodo.next
            print(fila)
            fila_actual = fila_actual.next

    def agregar_simbolos(self):
        simbolos = ["+"] * self.n + ["-"] * self.n
        random.shuffle(simbolos)
        nodos = []
        fila_actual = self.tablero.head
        while fila_actual:
            nodo = fila_actual.value.head
            while nodo:
                if nodo.value is None:
                    nodos.append(nodo)
                nodo = nodo.next
            fila_actual = fila_actual.next
        random.shuffle(nodos)
        for nodo in nodos:
            if simbolos:
                nodo.value = simbolos.pop()



