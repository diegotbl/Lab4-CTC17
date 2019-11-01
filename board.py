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

    def get_value_function(self, x, y):
        return self.board[x][y].get_value_function()

    def get_tag(self, x, y):
        return self.board[x][y].get_tag()

    def get_r(self, x, y):
        return self.board[x][y].get_r()

    def update_value_function(self, x, y, value_function_neighbor):
        self.board[x][y].update_value_function(value_function_neighbor)


class Cell:
    def __init__(self, content):
        self.content = content

    def get_r(self):
        return self.content.r

    def get_tag(self):
        return self.content.tag

    def get_value_function(self):
        return self.content.value_function

    def update_value_function(self, value_function_neighbor):
        self.content.value_function = max(value_function_neighbor[0], value_function_neighbor[1],
                                                                value_function_neighbor[2], value_function_neighbor[3])


class Wumpus:
    def __init__(self):
        self.name = "wumpus"
        self.r = -100
        self.tag = "W"
        self.value_function = 0


class Pit:
    def __init__(self):
        self.name = "pit"
        self.r = -50
        self.tag = "P"
        self.value_function = 0


class Gold:
    def __init__(self):
        self.name = "gold"
        self.r = 100
        self.tag = "G"
        self.value_function = 0


class Empty:
    def __init__(self):
        self.name = "empty"
        self.r = -0.1
        self.tag = "E"
        self.value_function = 0
