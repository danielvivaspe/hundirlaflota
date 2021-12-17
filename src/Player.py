import numpy as np
import pandas as pd
from string import ascii_letters
from playsound import playsound

import GameException


class Player:
    shotChar = 'X'
    defaultChar = '~'

    def __init__(self, boardSize, id, name):

        letters = pd.Series(list(ascii_letters.upper()[:boardSize]))

        self.publicBoard = pd.DataFrame(np.full([boardSize, boardSize], self.defaultChar), letters,
                                        columns=range(1, boardSize + 1))

        self.privateBoard = self.publicBoard.copy()
        self.data = {
            'id': id,
            'name': name,
            'shipChar': 'O',
            'wonGames': 0,
            'lostGames': 0
        }

    def getShipPoints(self, ship):
        """
        Genera una lista con todos los puntos del barco, extremos incluidos
        :param ship: La tupla del barco
        :return: lista con todos los puntos
        """

        points = []

        letters = list(ascii_letters.upper()[:self.publicBoard.shape[0]])

        x = self.getCoordLetterIndex(ship[1]) - self.getCoordLetterIndex(ship[0])
        y = int(ship[1][1:]) - int(ship[0][1:])

        if x == 0 and y != 0:  # El barco está en horizontal
            for i in range(0, y + 1):
                points.append(ship[0][0] + str(int(ship[0][1:]) + i))

        elif y == 0 and x != 0:  # El barco está en vertical
            for i in range(0, x + 1):
                points.append(letters[letters.index(ship[0][0]) + i] + ship[1][1:])

        else:  # El barco solo tiene un punto
            points.append(ship[0])

        return points

    def placeShip(self, ship):
        """
        Comprueba si el barco cabe o se sale del tablero
        :param ship: La tupla con las coordenadas del barco
        :return: True o False dependiendo de si entra o no
        """

        if self.shipFits(ship):
            for i in range(len(ship)):
                if self.positionState(ship[i]) != 1:
                    return False

        shipPoints = self.getShipPoints(ship)

        for i in shipPoints:
            self.privateBoard.loc[i[0]][int(i[1:])] = self.data['shipChar']

        return True

    def receiveShot(self, coord):
        """
        Recibe una disparo
        :param coord: La posicion disparada
        :return: Codigo de lo que habia en la posicion
        """

        playsound('../sound/shot.wav')

        # self.privateBoard[coord[0], coord[1]] = self.shotChar
        # self.publicBoard[coord[0], coord[1]] = self.shotChar

        code = self.positionState(coord)

        self.privateBoard.loc[coord[0]][int(coord[1:])] = self.shotChar
        self.publicBoard.loc[coord[0]][int(coord[1:])] = self.shotChar

        sound = f'../sound/shot_{code}.wav'
        playsound(sound)

        return code

    def positionState(self, pos):
        """
        Checks the state of the position
        :param pos: La posicion que se quiere comprobar
        :return: The position code
            1 - Free position
            2 - Shooted position
            3 - Ship position
        """

        if self.privateBoard.loc[pos[0]][int(pos[1:])] == self.defaultChar:
            return 1  # Free position
        elif self.privateBoard.loc[pos[0]][int(pos[1:])] == self.shotChar:
            return 2  # Shooted position
        elif self.privateBoard.loc[pos[0]][int(pos[1:])] == self.data['shipChar']:
            return 3  # Ship position

    def shipFits(self, ship):
        """
        Comprueba si un barco cabe en el tablero. No comprueba si hay otros barcos.
        :param ship: La tupla del barco a comprobar
        :return: True si cabe o False si no
        """

        shipPoints = self.getShipPoints(ship)

        for i in shipPoints:

            if (
                    (self.privateBoard.shape[0] + 1) <= self.getCoordLetterIndex(i[0]) or
                    (self.privateBoard.shape[1] + 1) <= int(i[1:])
            ):
                return False

        return True

    def shipRemaining(self):
        """
        Comprueba si quedan barcos sin disparar en el tablero
        :return: Int con la cantidad de posiciones de barcos sin disparar que quedan
        """
        return np.sum([self.privateBoard == self.data['shipChar']])

    def addShip(self, ship):
        """
        Comprueba si puede añadir un barco y lo añade si puede
        :param ship: Tupla con el barco (C1, D1)
        :return: True si ha podido ponerlo o False si no ha podido
        """
        # 1. Sacar lista de posiciones
        shipPoints = self.getShipPoints(ship)

        # 2. Comprobar si cabe
        fits = self.shipFits(ship)

        # 3. Colocar
        place = self.placeShip(ship)

        # 4. Devolver respuesta
        return fits and place

    def getCoordLetterIndex(self, pos):
        return ascii_letters.upper().index(pos[0]) + 1
