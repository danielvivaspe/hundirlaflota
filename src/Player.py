
import numpy as np
import GameException


class Player:
    shotChar = 'X'
    defaultChar = '~'

    def __init__(self, boardSize, id, name):
        # self.shots = np.empty_like((boardSize, boardSize))
        # self.ships = []
        self.board = np.full((boardSize, boardSize), self.defaultChar)
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

    def placeShip(self, shipPoints):

        for i in range(len(shipPoints)):
            if self.positionState(shipPoints[i]) == 2:
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
        #Sacar el maximo de la x y de la y
        #Si es mas que el tamaño, devuelve falso
        pass