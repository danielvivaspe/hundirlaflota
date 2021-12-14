from Player import Player
from GameException import GameException

player = Player(10, 1, "Daniel")


def textException():
    raise GameException(code=1, data={'position': (2, 3)})


def testShipFits():
    print(player.shipFits((1, 2), (1, 9)))


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

try:
    tmp = 2 / 0


except:
    print('error')



