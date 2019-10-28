class Board:
    def __init__(self):
        """ Creates the world with wumpus, gold and pits, as displayed on the project's description """
        self.board = []

        wumpus = Wumpus()
        pit = Pit()
        gold = Gold()
        empty = Empty()

        self.board.append([Cell(empty), Cell(empty), Cell(wumpus), Cell(empty)])
        self.board.append([Cell(empty), Cell(empty), Cell(gold), Cell(pit)])
        self.board.append([Cell(pit), Cell(empty), Cell(pit), Cell(empty)])
        self.board.append([Cell(empty), Cell(empty), Cell(empty), Cell(empty)])
        self.board.append([Cell(empty), Cell(wumpus), Cell(empty), Cell(empty)])
        self.board.append([Cell(empty), Cell(gold), Cell(empty), Cell(empty)])
        self.board.append([Cell(pit), Cell(empty), Cell(pit), Cell(pit)])
        self.board.append([Cell(empty), Cell(empty), Cell(empty), Cell(empty)])

    def print(self):
        for y in [3, 2, 1, 0]:
            for x in range(8):
                print(self.board[x][y].content.tag, end="\t")
            print()
        print()


class Cell:
    def __init__(self, content):
        self.content = content


class Wumpus:
    def __init__(self):
        self.name = "wumpus"
        self.r = -100
        self.tag = "W"


class Pit:
    def __init__(self):
        self.name = "pit"
        self.r = -50
        self.tag = "P"


class Gold:
    def __init__(self):
        self.name = "gold"
        self.r = 100
        self.tag = "G"


class Empty:
    def __init__(self):
        self.name = "empty"
        self.r = 0
        self.tag = "E"
