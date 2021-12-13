import numpy as np


class Game:

    def __init__(self, boardSize):
        tablero = np.full((boardSize, boardSize), "~")
