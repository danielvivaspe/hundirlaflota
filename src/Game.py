import random
import string

from Player import Player
#import GameException#<---todo ¿Borrar?


class Game:
    player_1 = None
    player_computer = None
    id_player = 10#int(random.randint(1, 99))<--- todo Volver a poner cuando se resuelva
    id_computer = 9#int(random.randint(1, 99))<---todo Volver a poner cuando se resuelva
    size_abc=None
    boardSize=10
    #lista_Final=[]#<--- todo quiero crear esta lista global, pero no puedo
    #<---todo podríamos crear aquí el tablero


    def __init__(self):
        self.printMenu()


    #def play(self):#<---todo Borrar cuando estemos seguros
    #    self.printMenu()



    def printMenu(self):
        option = (int(input("Pulsa 1 para Jugar//Pulsa 2 para Salir//Pulsa 3 para ver los Créditos")))
        #<---todo ¿Poner un Manual de uso?
        while option != 2:
            if option == 1:
                print("START")
                self.askForData()
            elif option == 3:
                print("CREDITS\n·Daniel Vivas\n·Fernando Bielza")
                option = (int(input("Pulsa 1 para Jugar//Pulsa 2 para Salir//Pulsa 3 para ver los Créditos")))
            else:
                option = (int(input("Por favor, introduce una opción disponible.\nPulsa 1 para Jugar//Pulsa 2 para Salir//Pulsa 3 para ver los Créditos")))
        print("EXIT.\nMuchas gracias por jugar")



    def askForData(self):
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
        self.makeComputerShips()


    def makeComputerShips(self):
        ship_4 = [(1, 3)]
        ship_3 = [(1, 2), (2, 2)]
        ship_2 = [(1, 1), (2, 1), (3, 1)]
        ship_1 = [(1, 0), (2, 0), (3, 0), (4, 0)]
        lista_BARCOS = [ship_4[0], ship_3[0], ship_3[1], ship_2[0], ship_2[1], ship_2[2], ship_1[0], ship_1[1],
                        ship_1[2],
                        ship_1[3]]
        lista_Final = []
        for i in lista_BARCOS:
            fit_on = False
            while not fit_on:
                proa = str(self.size_abc[random.randint(0, self.boardSize - 1)]) + str(random.randint(1, self.boardSize))
                if i[1] != 0:
                    popa = random.randint(1, 4)
                    if popa == 1:
                        ship = self.steerUp(proa, i)
                    elif popa == 2:
                        ship = self.steerDown(proa, i)
                    elif popa == 3:
                        ship = self.steerRight(proa, i)
                    else:
                        ship = self.steerLeft(proa, i)
                else:
                    ship = (proa, proa)  # <--- todo ¿Esto es necesario?
                fit_on = Player.addShip(self, i)
            lista_Final.append(ship)
        print(lista_Final)
        self.makePlayerShip()



    def makePlayerShip(self):
        ship_4 = [(1, 3)]
        ship_3 = [(1, 2), (2, 2)]
        ship_2 = [(1, 1), (2, 1), (3, 1)]
        ship_1 = [(1, 0), (2, 0), (3, 0), (4, 0)]
        lista_BARCOS = [ship_4[0], ship_3[0], ship_3[1], ship_2[0], ship_2[1], ship_2[2], ship_1[0], ship_1[1], ship_1[2],
                        ship_1[3]]
        lista_Final = []
        for i in lista_BARCOS:
            fit_on = False
            while not fit_on:
                proa = input(f"¿Dónde se encuentra la proa de tu {i[0]}º barco de {int(i[1]) + 1} posiciones?: ")
                while proa[0] not in self.size_abc or int(proa[1:]) > self.boardSize:
                    proa = input("¡ERROR!\nLas coordenadas del disparo deben de estar dentro del tablero")
                if i[1] != 0:
                    popa = input(
                        "¿Hacia dónde está orientada la popa?\n¿Hacia ARRIBA(1)?¿Hacia ABAJO(2)?¿Hacia la DERECHA(3)? ¿O hacia la IZQUIERDA(4)")
                    while popa.upper != "ARRIBA" and popa.upper != "ABAJO" and popa.upper != "DERECHA" and popa.upper != "IZQUIERDA" and popa != "1" and popa != "2" and popa != "3" and popa != "4":
                        popa = input(
                            "Por favor, introduzca una opción válida\n¿Hacia dónde está orientada la popa?\n¿Hacia ARRIBA(1)?¿Hacia ABAJO(2)?¿Hacia la DERECHA(3)? ¿O hacia la IZQUIERDA(4)")
                    if popa == "1" or popa.upper == "ARRIBA":
                        ship = self.steerUp(proa, i)
                    elif popa == "2" or popa.upper == "ABAJO":
                        ship = self.steerDown(proa, i)
                    elif popa == "3" or popa.upper == "DERECHA":
                        ship = self.steerRight(proa, i)
                    else:
                        ship = self.steerLeft(proa, i)
                else:
                    ship = (proa, proa)  # <--- todo ¿Esto es necesario?
                fit_on = Player.addShip(self, i)
            lista_Final.append(ship)
        print("Así queda distribuida tu flota", lista_Final)
        self.startBattle()



    def steerUp(self, proa, i):
        indice_abc = self.size_abc.index(proa[0])
        letter_indice_abc = indice_abc - i[1]
        popa = self.size_abc[letter_indice_abc] + proa[1:]
        ship = (proa, popa)
        return ship


    def steerDown(self, proa, i):
        indice_abc = self.size_abc.index(proa[0])
        letter_indice_abc = indice_abc + i[1]
        popa = self.size_abc[letter_indice_abc] + proa[1:]#<--- todo ¡CUIDADO CON EL RANGO!
        ship = (proa, popa)
        return ship


    def steerRight(self, proa, i):
        popa = proa[0] + str(int(proa[1:]) + int(i[1]))
        ship = (proa, popa)
        return ship


    def steerLeft(self, proa, i):
        popa = proa[0] + str(int(proa[1:]) - int(i[1]))
        ship = (proa, popa)
        return ship



    def startBattle(self):
        if self.id_player >= self.id_computer:
            print ("¡COMIENZA JUGANDO EL JUGADOR!")
            self.shootingShiftPlayer()
        else:
            print ("¡COMIENZA JUGANDO EL RIVAL!")
            self.shootingShiftComputer()



    def shootingShiftPlayer(self):
        #print (escenario)#<---todo poner cuando esté listo
        playerTurn = input("¿Hacia dónde quieres dirigir tu disparo?: ")
        while playerTurn[0] not in self.size_abc or int(playerTurn[1:]) > self.boardSize:
            playerTurn = input ("¡ERROR!\nLas coordenadas del disparo deben de caer dentro del tablero")
        print(f"Tu disparo fue a parar a {playerTurn}")
        result=self.player_computer.receiveShot(playerTurn)
        while result == 3:
            print ("¡BLANCO!")
            check = self.player_computer.shipRemains()  # <---todo validar coordenadas de barco
            if check == True:
                self.computerDefeat()
            playerTurn = input("Tienes un nuevo disparo ¿Hacia dónde quieres dirigirlo?: ")
            while playerTurn[0] not in self.size_abc or int(playerTurn[1:]) > self.boardSize:
                playerTurn = input("¡ERROR!\nLas coordenadas del disparo deben de caer dentro del tablero")
            print(f"Tu disparo fue a parar a {playerTurn}")
            result = self.player_computer.receiveShot(playerTurn)
        if result == 2:
            print ("Tiro fallado. La posición ya había sido atacada")
        else:
            print ("Tiro fallado.")
        self.shootingShiftComputer()



    def shootingShiftComputer(self):
        computerTurn = str (self.size_abc[random.randint(0, self.boardSize-1)]) + str(random.randint(1, self.boardSize))
        result=self.player_1.receiveShot(computerTurn)
        while result == 3 or result == 2:
            if result == 3:
                print(f"Tu rival disparó a la posición {computerTurn[0]}{computerTurn[1]}")
                print("¡BLANCO!")
                check=self.player_computer.shipRemains()# <---todo validar coordenadas de barco
                if check == True:
                    self.playerDefeat()
            computerTurn = str (self.size_abc[random.randint(0, self.boardSize-1)]) + str(random.randint(1, self.boardSize))
            result = self.player_computer.receiveShot(computerTurn)
        if result == 1:
            print(f"Tu rival disparó a la posición {computerTurn[0]}{computerTurn[1]}")
            print("Tiro fallado.")
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
