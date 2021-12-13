class GameException(Exception):

    def __init__(self, code, data):

        super().__init__(code)
        self.code = code
        self.data = data

        print(self.getExceptionInfo())


    def getExceptionInfo(self):
        if self.code == 1:
            return f"Trying to place a ship on position {self.data['position']} with a ship already"
