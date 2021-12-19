import random
import string

from Player import Player
from playsound import playsound


class Game:
    player_1 = None
    player_computer = None
    id_player = int(random.randint(1, 99))
    id_computer = int(random.randint(1, 99))
    size_abc=None
    boardSize=10
    ship_4 = [(1, 3)]
    ship_3 = [(1, 2), (2, 2)]
    ship_2 = [(1, 1), (2, 1), (3, 1)]
    ship_1 = [(1, 0), (2, 0), (3, 0), (4, 0)]
    lista_BARCOS = [ship_4[0], ship_3[0], ship_3[1], ship_2[0], ship_2[1], ship_2[2], ship_1[0], ship_1[1], ship_1[2],
                    ship_1[3]]


    def __init__(self):
        print('###################### BIENVENIDO A HUNDIR LA FLOTA ######################')
        print('################### By Daniel Vivas y Fernando Bielza ####################')
        self.printMenu()

    def play (self):
        self.askForData()
        self.makeComputerShips()
        self.makePlayerShip()
        self.startBattle()

    def printMenu(self):
        option = "0"
        while option != "2":

            print("Pulsa 1 para jugar")
            print("Pulsa 2 para salir")
            print("Pulsa 3 para ver los créditos")
            option = input(">> ")

            if option == "1":
                print("START")
                self.play()

            elif option == "2":
                print("Gracias por jugar.")
                return

            elif option == "3":
                print("CREDITS\n·Daniel Vivas\n·Fernando Bielza")

            else:
                print("Por favor, elige una opción correcta")


    def printMenu_2(self):
        option = (int(input("=====================================MENÚ======================================\n>Pulsa [1] para Jugar/·/Pulsa [2] para Salir/·/Pulsa [3] para ver los Créditos<\n===============================================================================\n")))
        while option != 2:
            if option == 1:
                print("_______________________________________________________________________________\n\n>·>·>·>·>·>·>·>·>·>·>·>·>·>·>·>·>·>·START·<·<·<·<·<·<·<·<·<·<·<·<·<·<·<·<·<·<·<\n_______________________________________________________________________________\n\n")
                self.askForData()
            elif option == 3:
                print("····································CREDITS····································\n--->Daniel Vivas\n--->Fernando Bielza\n···············································································\n\n")
                option = (int(input("=====================================MENÚ======================================\n>Pulsa [1] para Jugar/·/Pulsa [2] para Salir/·/Pulsa [3] para ver los Créditos<\n===============================================================================\n")))
            else:
                option = (int(input("\¡ERROR!\n-------------------------------------------------------------------------------\nPor favor, introduce una opción disponible.\n\n=====================================MENÚ======================================\n>Pulsa [1] para Jugar/·/Pulsa [2] para Salir/·/Pulsa [3] para ver los Créditos<\n===============================================================================\n")))
        print("\n\n\n                                ....{EXIT}...\n                            Muchas gracias por jugar")



    def askForData(self):
        ask=0
        while ask == 0:
            name = input("·Por favor, indica cual es el nombre del JUGADOR: \n")
            while len(name) == 0 or len(name) > 15:
                name = input("-------------------------------------------------------------------------------\n¡DIMENSIONES ERRÓNEAS!\n-------------------------------------------------------------------------------\nPor favor, escoge un nombre con una dimensión superior a 0 e inferior a 16\ncaracteres: ")
            self.boardSize = int(input(f"\n·Muy bien, {name}, ahora indica cuales son las dimensiones del tablero de juego\n(con un valor comprendido entre [5] y [20]): \n"))
            while self.boardSize < 5 or self.boardSize > 20:
                self.boardSize = int(input("-------------------------------------------------------------------------------\n¡DATO ERRÓNEO!\n-------------------------------------------------------------------------------\nPor favor, asegúrate de que el valor esté comprendido entre [5] y [20]: \n"))
            print (f"\n·DATOS INTRODUCIDOS:\nNombre del JUGADOR: {name}/·/Dimensiones del tablero: {self.boardSize}.\n")
            result = input ("·¿Estás deacuerdo con tus datos? (si quieres sobreescribirlos, pulsa [1]) \n")
            if result != "1":
                ask=1
            else:
                print("-------------------------------------------------------------------------------\nDATOS REMOVIDOS\n-------------------------------------------------------------------------------")
        self.size_abc = list(string.ascii_lowercase.upper())[:(self.boardSize)]
        self.player_computer = Player(self.boardSize, self.id_computer, "Computer")
        self.player_1 = Player(self.boardSize, self.id_player, name)

        print("\n\n>·>·>·>·>·>·>·>·>·>·>·>·>·>·>·DATOS APLICADOS·<·<·<·<·<·<·<·<·<·<·<·<·<·<·<·<")
        print(f"·Nombre del JUGADOR: [{name}]/·/Dimensiones del tablero: [{self.boardSize}x{self.boardSize}]/·/Id: [{self.id_player}]")
        print(f"·Nombre del RIVAL: [Computadora]/·/Dimensiones del tablero: [{self.boardSize}x{self.boardSize}]/·/Id: [{self.id_computer}]\n\n")


    def makeComputerShips(self):
        for i in self.lista_BARCOS:
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
                    ship = (proa, proa)
                fit_on = self.player_computer.addShip(ship)#<---todo en ocasiones, da error aquí, en la linea 155->49 de Player


    def makePlayerShip(self):
        print("\n\n>·>·>·>·>·>·>·>·>·>·>·>·>·>·>·EDITOR DE FLOTA·<·<·<·<·<·<·<·<·<·<·<·<·<·<·<·<")
        for i in self.lista_BARCOS:
            fit_on = False
            while not fit_on:
                proa = input(f"·¿Dónde se encuentra la proa de tu {i[0]}º barco de [{int(i[1]) + 1}] posiciones?: ").upper()
                while proa[0] not in self.size_abc or int(proa[1:]) > self.boardSize:
                    print("¡ERROR!\n·Las coordenadas deben de estar dentro del tablero")
                    proa = input(f"·¿Dónde se encuentra la proa de tu {i[0]}º barco de [{int(i[1]) + 1}] posiciones?: ").upper()
                if i[1] != 0:
                    popa = input(
                        "·¿Hacia dónde está orientada la popa?\n¿Hacia ARRIBA[1]?¿Hacia ABAJO[2]?¿Hacia la DERECHA[3]? ¿O hacia la IZQUIERDA[4]?: ").upper()
                    while popa.upper != "ARRIBA" and popa.upper != "ABAJO" and popa.upper != "DERECHA" and popa.upper != "IZQUIERDA" and popa != "1" and popa != "2" and popa != "3" and popa != "4":
                        popa = input(
                            "¡ERROR!\nPor favor, introduzca una opción válida\n·¿Hacia dónde está orientada la popa?\n¿Hacia ARRIBA[1]?¿Hacia ABAJO[2]?¿Hacia la DERECHA[3]? ¿O hacia la IZQUIERDA[4]?: ").upper()
                    if popa == "1" or popa.upper == "ARRIBA":
                        ship = self.steerUp(proa, i)
                    elif popa == "2" or popa.upper == "ABAJO":
                        ship = self.steerDown(proa, i)
                    elif popa == "3" or popa.upper == "DERECHA":
                        ship = self.steerRight(proa, i)
                    else:
                        ship = self.steerLeft(proa, i)
                else:
                    ship = (proa, proa)
                fit_on = self.player_1.addShip(ship)
                if fit_on ==False:
                    print ("¡ERROR! El barco no pudo ser introducido en el tablero. Por favor, prueba otras coordenadas.")
            print(f"\nTu [Flota]:\n", self.player_1.privateBoard)

    def steerUp(self, proa, i):
        indice_abc = self.size_abc.index(proa[0])
        letter_indice_abc = indice_abc - i[1]
        popa = list(string.ascii_lowercase.upper())[letter_indice_abc] + proa[1:]#<--todo
        ship = (popa, proa)
        return ship


    def steerDown(self, proa, i):
        indice_abc = self.size_abc.index(proa[0])
        letter_indice_abc = indice_abc + i[1]
        popa = list(string.ascii_lowercase.upper())[letter_indice_abc] + proa[1:]#<---todo ¡CUIDADO! A veces da ERROR
        #popa = self.size_abc[letter_indice_abc] + proa[1:]#<--- todo ¡CUIDADO! A veces da ERROR
        ship = (proa, popa)
        return ship


    def steerRight(self, proa, i):
        popa = proa[0] + str(int(proa[1:]) + int(i[1]))
        ship = (proa, popa)
        return ship


    def steerLeft(self, proa, i):
        popa = proa[0] + str(int(proa[1:]) - int(i[1]))
        ship = (popa, proa)
        return ship



    def startBattle(self):
        if self.id_player >= self.id_computer:
            print("\n>·>·>·>·>·>·>·>·>·>·>·>·¡COMIENZA JUGANDO EL JUGADOR!·<·<·<·<·<·<·<·<·<·<·<·<")
            self.shootingShiftPlayer()
        else:
            print("\n>·>·>·>·>·>·>·>·>·>·>·>·>·¡COMIENZA JUGANDO EL RIVAL!·<·<·<·<·<·<·<·<·<·<·<·<")
            self.shootingShiftComputer()



    def shootingShiftPlayer(self):
        playerTurn = input("\n·¿Hacia dónde quieres dirigir tu disparo?: ").upper()
        while playerTurn[0] not in self.size_abc or int(playerTurn[1:]) > self.boardSize:
            print ("¡ERROR!\nLas coordenadas del disparo deben de caer dentro del tablero.")
            playerTurn = input ("·¿Hacia dónde quieres dirigir tu disparo?: ").upper()
        print(f"Tu disparo fue a parar a [{playerTurn}]")
        result=self.player_computer.receiveShot(playerTurn)
        while result == 3:
            print ("\n                              ¡¡¡BLANCO!!!                                  \n")
            print(f"\nTus [Disparos]:\n", self.player_computer.publicBoard)
            check = self.player_computer.shipRemaining()
            if check == 0:
                self.computerDefeat()
                return
            playerTurn = input("\n·Tienes un nuevo disparo ¿Hacia dónde quieres dirigirlo?: ").upper()
            while playerTurn[0] not in self.size_abc or int(playerTurn[1:]) > self.boardSize:
                print ("¡ERROR!\nLas coordenadas del disparo deben de caer dentro del tablero.")
                playerTurn = input("·¿Hacia dónde quieres dirigir tu disparo?: ").upper()
                #<--- todo ¿Poner aquí un sonido de "FAIL"?
            print(f"Tu disparo fue a parar a [{playerTurn}]")
            result = self.player_computer.receiveShot(playerTurn)
        if result == 2:#<---todo disparé a una posición nueva, y me dio como repetida (el pc disparó a esa posición antes, a lo mejor por eso...)
            print ("Tiro fallado. La posición ya había sido atacada")
        else:
            print ("Tiro fallado.")
        print(f"\nTus [Disparos]:\n", self.player_computer.publicBoard)
        self.shootingShiftComputer()



    def shootingShiftComputer(self):
        print ("\n\n¡TU RIVAL ATACA!")
        computerTurn = str (self.size_abc[random.randint(0, self.boardSize-1)]) + str(random.randint(1, self.boardSize))
        print(f"\nTu rival disparó a la posición [{computerTurn[0]}{computerTurn[1:]}]")
        result=self.player_1.receiveShot(computerTurn)
        while result == 3 or result == 2:#<---todo Cuando la máquina saca un "2", hace sonido de disparo repetido
            if result == 3:#<---todo en una partida, disparó a una posoción donde yo no tenía barco, y aún así impactó
                print("\n                              ¡¡¡BLANCO!!!                                  \n")
                print(f"\nTu rival disparó a la posición [{computerTurn[0]}{computerTurn[1:]}]")
                check=self.player_1.shipRemaining()
                if check == 0:
                    self.playerDefeat()
                    return
            computerTurn = str (self.size_abc[random.randint(0, self.boardSize-1)]) + str(random.randint(1, self.boardSize))
            result = self.player_1.receiveShot(computerTurn)
        if result == 1:
            print(f"\n\nTu rival disparó a la posición [{computerTurn[0]}{computerTurn[1:]}]")
            print("Tiro fallado.")
        print(f"\nTu [Flota]:\n", self.player_1.privateBoard)
        self.shootingShiftPlayer()



    def playerDefeat (self):
        playsound('../sound/defeat.wav')  # <---todo creo que este sonido es un simple sonido de disparo
        print ("Tu último barco ha sido hundido. Ya no te quedan más efectivos operativos.")
        print("\n\n                        ...{Has sido derrotado}...\n")

    def computerDefeat (self):
        playsound('../sound/victory.wav')#<---todo ¿No sería mejor adelante?
        print ("Ya no quedan más navíos operativos. La flota rival ha sido hundida.")
        print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~¡VICTORIA!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Has ganado la Partida. Tus barcos regresan a casa.\n")

