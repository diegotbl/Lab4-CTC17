from random import randint
from math import pow

class Robot:
    def __init__(self, board):
        self.x = 0
        self.y = 0
        restarted = True
        self.acc_r = 0
        while restarted is True:
            restarted = self.restart(board)

    def randomize_pos(self, board):
        self.x = randint(0, 7)
        self.y = randint(0, 3)


    def update_pos(self, x, y):
        self.x = x
        self.y = y

    def move(self, mov, board):
        if mov == 0:
            print("\tMoving up. ", end="")
            if self.y == 3:         # can't go up
                print("Bump")
                return -1                # edge collision cost
            else:
                return board.get_value_function(self.x, self.y + 1)
        elif mov == 1:
            print("\tMoving right. ", end="")
            if self.x == 7:
                print("Bump")
                return -1  # edge collision cost
            else:
                return board.get_value_function(self.x + 1, self.y)
        elif mov == 2:
            print("\tMoving down. ", end="")
            if self.y == 0:
                print("Bump")
                return -1  # edge collision cost
            else:
                return board.get_value_function(self.x, self.y - 1)
        elif mov == 3:
            print("\tMoving left. ", end="")
            if self.x == 0:
                print("Bump")
                return -1  # edge collision cost
            else:
                return board.get_value_function(self.x - 1, self.y)

    def try_move(self, mov, board, gama, time):
        """ Moves robot according to it's defects """
        if mov == 0:
            print("\nTrying to move up.\n")
        elif mov == 1:
            print("\nTrying to move right.\n")
        elif mov == 2:
            print("\nTrying to move down.\n")
        elif mov == 3:
            print("\nTrying to move left.\n")

        expected_reward = 0
        mov1 = (mov + 3) % 4
        mov2 = (mov + 1) % 4
        expected_reward = board.get_r(self.x, self.y) + (pow(gama, time))*(0.2*self.move(mov1, board) + 0.7*self.move(mov, board) + 0.1*self.move(mov2, board))
        return expected_reward

    def restart(self, board):
        """ Decides whether it should be restarted or not and restarts if necessary.
            Returns True if restarted and False otherwise. """
        cell_content = board.board[self.x][self.y].content.name
        if cell_content == "wumpus" or cell_content == "pit" or cell_content == "gold":
            print("\tRestarting... ", end="")
            self.randomize_pos(board)
            self.acc_r += -0.1          # Restart is considered a movement
            print(self)
            return True
        return False

    def __str__(self):
        r = round(self.acc_r, 1)
        return "Robot is on (" + str(self.x) + ", " + str(self.y) + "). Accumulated reinforcement: " + str(r)
