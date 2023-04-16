from abc import ABC


class Character(ABC):
    def __init__(self):
        self.vida = 50

    def move(self):
        pass


class Alien(Character):
    def __init__(self):
        super().__init__()

    def move(self):
        pass

    def attack(self):
        pass


class Pedrator(Character):
    def __init__(self):
        super().__init__()

    def move(self):
        pass

