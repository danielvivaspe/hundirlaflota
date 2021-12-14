
import numpy as np
import pandas as pd
from string import ascii_letters

import GameException


class Player:
    shotChar = 'X'
    defaultChar = '~'

    def __init__(self, boardSize, id, name):

        letters = pd.Series(list(ascii_letters.upper()[:boardSize]))

        self.publicBoard = pd.DataFrame(np.full([boardSize, boardSize], self.defaultChar), letters)

        self.privateBoard = self.publicBoard.copy()
        self.data = {
            'id': id,
            'name': name,
            'shipChar': 'O',
            'wonGames': 0,
            'lostGames': 0
        }


    def getShipPoints(self, cStart, cEnd):
        # It will return a list of coords where the ship should be placed

        points = []

        list(cStart)[0]


        x = cEnd[0] - cStart[0]
        y = cEnd[1] - cStart[1]

        if x == 0 and y != 0:  # El barco está en horizontal
            for i in range(0, y + 1):
                points.append((cStart[0], cStart[1] + i))

        elif y == 0 and x != 0:  # El barco está en vertical
            for i in range(0, x + 1):
                points.append((cStart[0] + i, cStart[1]))

        else:  # El barco solo tiene un punto
            points.append(cStart)

        return points

    def getShipPoints2(self, cStart, cEnd):
        # It will return a list of coords where the ship should be placed

        points = []

        letters = pd.Series(list(ascii_letters.upper()[:self.publicBoard.shape[0]]))
        list(cStart)[0]

        x = letters.index(list(cEnd)[0]) - letters.index(list(cStart)[0])
        y = int(cEnd[1:]) - int(cStart[1:])

        if x == 0 and y != 0:  # El barco está en horizontal
            for i in range(0, y + 1):
                points.append((cStart[0], cStart[1] + i))

        elif y == 0 and x != 0:  # El barco está en vertical
            for i in range(0, x + 1):
                points.append((cStart[0] + i, cStart[1]))

        else:  # El barco solo tiene un punto
            points.append(cStart)

        return points

    def placeShip(self, shipPoints):

        for i in range(len(shipPoints)):
            if self.positionState(shipPoints[i]) == 1:
                raise GameException(1, {'position': shipPoints[i]})

        for i in range(len(shipPoints)):
            self.board[shipPoints[i][0]][shipPoints[i][1]] = self.data['shipChar']

    def receiveShot(self, coord):
        self.board[coord[0], coord[1]] = self.shotChar

    def positionState(self, coord):
        """
        Checks the state of the position
        :param coord:
        :return: The position code
            1 - Free position
            2 - Shooted position
            3 - Ship position
        """
        if self.board[coord[0]][coord[1]] == self.defaultChar:
            return 1  # Free position
        elif self.board[coord[0]][coord[1]] == self.shotChar:
            return 2  # Shooted position
        elif self.board[coord[0]][coord[1]] == self.data['shipChar']:
            return 3 #  Ship position

    def shipFits(self, cStart, cEnd):

        #tamano del tablero > maximo de las coordenadas x o y
        # Si el maximo de las coordenadas de x o y es mayor que el tamano, se sale

        if (
                self.board.shape[0] > (max(cStart[0], cEnd[0])) and
                self.board.shape[0] > (max(cStart[1], cEnd[1]))
        ):
            return True

        return False


