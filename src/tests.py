from Player import Player
from GameException import GameException

player = Player(10, 1, "Daniel")


def textException():
    raise GameException(code=1, data={'position': (2, 3)})


jugador = Player('Ana').re
maquina = Player('Maquina').receiveShot()


def testPlaceShip():
    points = player.getShipPoints((1, 2), (1, 4))

    player.placeShip(points)

    print(player.board)


def testGetShipPoints():
    print(player.getShipPoints((1, 2), (1, 4)))
    print('\n\n')
    print(player.getShipPoints((2, 1), (4, 1)))

    print('\n\n')
    print(player.getShipPoints((2, 1), (2, 1)))


testGetShipPoints()