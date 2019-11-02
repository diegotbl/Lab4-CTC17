class Board:
    def __init__(self):
        """ Creates the world with wumpus, gold and pits, as displayed on the project's description """
        self.board = []

        self.board.append([Cell(Empty()), Cell(Empty()), Cell(Wumpus()), Cell(Empty())])
        self.board.append([Cell(Empty()), Cell(Empty()), Cell(Gold()), Cell(Pit())])
        self.board.append([Cell(Pit()), Cell(Empty()), Cell(Pit()), Cell(Empty())])
        self.board.append([Cell(Empty()), Cell(Empty()), Cell(Empty()), Cell(Empty())])
        self.board.append([Cell(Empty()), Cell(Wumpus()), Cell(Empty()), Cell(Empty())])
        self.board.append([Cell(Empty()), Cell(Gold()), Cell(Empty()), Cell(Empty())])
        self.board.append([Cell(Pit()), Cell(Empty()), Cell(Pit()), Cell(Pit())])
        self.board.append([Cell(Empty()), Cell(Empty()), Cell(Empty()), Cell(Empty())])

    def print(self):
        for y in [3, 2, 1, 0]:
            for x in range(8):
                print(self.board[x][y].content.tag, end="\t")
            print()
        print()

    def show_value_funtion(self):
        for y in [3, 2, 1, 0]:
            for x in range(8):
                print(self.board[x][y].content.value_function, end="\t")
            print()
        print()

    def get_value_function(self, x, y):
        return self.board[x][y].get_value_function()

    def get_tag(self, x, y):
        return self.board[x][y].get_tag()

    def get_r(self, x, y):
        return self.board[x][y].get_r()

    def update_value_function(self, x, y, value_function_neighbor):
        # print(value_function_neighbor)
        # print(x, y)
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
        self.content.value_function = max(value_function_neighbor)


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
