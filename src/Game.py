import random
import string

from Player import Player
#import GameException


class Game:
    player_1 = None
    player_computer = None
    id_player = int(random.randint(1, 99))
    id_computer = int(random.randint(1, 99))
    size_abc=None
    boardSize=10



    def __init__(self):
        pass



    def play(self):
        self.printMenu()



    def printMenu(self):
        option = (int(input("Pulsa 1 para Jugar//Pulsa 2 para Salir//Pulsa 3 para ver los Créditos")))
        while option != 2:
            if option == 1:
                print("START")
                self.askForData()
            elif option == 3:
                print("CREDITS")
                option = (int(input("Pulsa 1 para Jugar//Pulsa 2 para Salir//Pulsa 3 para ver los Créditos")))
            else:
                option = (int(input("Por favor, introduce una opción disponible.\nPulsa 1 para Jugar//Pulsa 2 para Salir//Pulsa 3 para ver los Créditos")))
        print("EXIT.\nMuchas gracias por jugar")



    def askForData(self):  # <---Para obtener los datos del jugador y del tablero
        ask=0
        while ask == 0:
            name = input("Por favor, indica cual es el nombre del JUGADOR: ")
            while len(name) == 0 or len(name) > 15:
                name = input("¡DIMENSIONES ERRÓNEAS!\nPor favor, escoge otro nombre con una dimensión superior a 0 e inferior a 16 caracteres:")
            self.boardSize = int(input(f"Muy bien, {name}, ahora indica cuales son las dimensiones del tablero de juego (con un valor comprendido entre 5 y 26): "))
            while self.boardSize < 5 or self.boardSize > 26:
                self.boardSize = int(input("¡DATO ERRÓNEO!\nPor favor, asegúrate de que el valor esté comprendido entre 5 y 26: "))
            print (f"Datos introducidos: Nombre del JUGADOR: {name}; Dimensiones del tablero: {self.boardSize}.")
            result = input ("¿Estás deacuerdo con tus datos? Si quieres sobreescribirlos, pulsa 1")
            if result != "1":
                ask=1
        self.size_abc = list(string.ascii_lowercase.upper())[:(self.boardSize)]
        self.player_computer = Player(self.boardSize, self.id_computer, "Computer")
        self.player_1 = Player(self.boardSize, self.id_player, name)

        print("DATOS CORRECTOS")
        print(f"Nombre del JUGADOR: {name}; Dimensiones del tablero: {self.boardSize}x{self.boardSize}; Id: {self.id_player}")
        print(f"Nombre del RIVAL: Computadora; Dimensiones del tablero: {self.boardSize}x{self.boardSize}; Id: {self.id_computer}")
        self.startBattle()



    def startBattle(self):
        #self.makeShips()<----------------------------------------------------------------------------------
        if self.id_player >= self.id_computer:
            print ("¡COMIENZA JUGANDO EL JUGADOR!")
            self.shootingShiftPlayer()
        else:
            print ("¡COMIENZA JUGANDO EL RIVAL!")
            self.shootingShiftComputer()



    def makeShips(self):  # <---crear los barcos uno a uno en forma de tuplas con una cordenada de inicio y una de fin (A,1), con bucle
        #ship_4= (4,)
        #ship_3= (3,3)
        #ship_2= (2,2,2)
        #ship_1= (1,1,1,1)
        lista = [("A1", "D1"), ("B2", "D2"), ("A2", "A3")]  # <---Lista con 3 barco
        for i in lista:
            ship=False
            while ship == False:
                ship = Player.addShip(self, i)
        # Si devuelve True, bien, Si devuelve False, no ha logrado poner el barco.
        # variable=playShip()
        # En caso de False, poner "raise GameException(1, {'position':x})" o un print ("No se puede")



    def shootingShiftPlayer(self):
        playerTurn = input("¿Hacia dónde quieres dirigir tu disparo?: ")
        while playerTurn[0] not in self.size_abc or int(playerTurn[1:]) > self.boardSize:
            playerTurn = input ("¡ERROR!\nLas coordenadas del disparo deben de caer dentro del tablero")
        print(f"Tu disparo fue a parar a {playerTurn}")
        #result=self.player_computer.receiveShot(playerTurn)
        result=3 #>---Todo quitar el resultado a piñón
        while result == 3:
            print ("¡BLANCO!")
            playerTurn = input("Tienes un nuevo disparo ¿Hacia dónde quieres dirigirlo?: ")
            while playerTurn[0] not in self.size_abc or int(playerTurn[1:]) > self.boardSize:
                playerTurn = input("¡ERROR!\nLas coordenadas del disparo deben de caer dentro del tablero")
            print(f"Tu disparo fue a parar a {playerTurn}")
            #result = self.player_computer.receiveShot(playerTurn)
            result=2
        if result == 2:
            print ("Tiro fallado. La posición ya ha sido atacada")
        else:
            print ("Tiro fallado.")
        self.shootingShiftComputer()



    def shootingShiftComputer(self):
        computerTurn = self.size_abc[random.randint(0, self.boardSize-1)], str(random.randint(1, self.boardSize))
        print(f"Tu rival disparó a la posición {computerTurn[0]}{computerTurn[1]}")
        #result=self.player_1.receiveShot(computerTurn)
        result=3
        while result == 3 o result == 2:
            print("¡BLANCO!")
            computerTurn = self.size_abc[random.randint(0, self.boardSize-1)], str(random.randint(1, self.boardSize))
            print(f"Tu rival disparó a la posición {computerTurn[0]}{computerTurn[1]}")
            #result = self.player_computer.receiveShot(computerTurn)
            result=2
        if result == 1:
            print("Tiro fallado.")
            #<-----Todo llamar a Player cuantos O hay (¿Quedan barcos? True o False) shipRemains()
        self.shootingShiftPlayer()



    def playerDefeat (self):
        print ("Tu flota ha sido hundida. Gana el RIVAL.")
        self.endGame()

    def computerDefeat (self):
        print ("¡VICTORIA! La flota rival ha sido hundida. Has ganado la partida.")
        self.endGame()



    def endGame (self):
        print ("Fin de la Partida.")
        self.printMenu()

