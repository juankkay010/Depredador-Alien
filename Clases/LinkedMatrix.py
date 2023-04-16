import random

from Clases.Node import Node


class LinkedMatrix:
    def __init__(self, n):
        self.n = n
        self.matrix = [[Node(None) for j in range(self.n)] for i in range(self.n)]  # Empty Matrix
        self.linked_nodes()  # Enlaza los nodos vacios
        self.simbolos_in_matrix()  # Agrega los simbolos a la matriz aleatoriamente

    def __getitem__(self, index):
        return self.matrix[index]

    def linked_nodes(self):
        for i in range(self.n):   # Recorre los nodos
            for j in range(self.n):
                node = self.matrix[i][j]  # Asigna los nodos

                # Verifica si el nodo actual tiene posiciones adyacentes y los enlaza
                if j > 0:
                    node.left = self.matrix[i][j-1]
                if j < self.n-1:
                    node.right = self.matrix[i][j+1]
                if i > 0:
                    node.top = self.matrix[i-1][j]
                if i < self.n-1:
                    node.bottom = self.matrix[i+1][j]

    def simbolos_in_matrix(self):
        simbolos = ["+", "-"]
        for i in range(self.n):
            for j in range(self.n):
                node = self.matrix[i][j]
                node.value = random.choice(simbolos)

    def print_matrix(self):
        n = len(self.matrix)
        for i in range(n):
            for j in range(n):
                print(self.matrix[i][j].value, end=" ")
            print()


if __name__ == "__main__":
    matrix = LinkedMatrix(4)
    matrix.print_matrix()


