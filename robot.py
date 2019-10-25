from random import randint


class Robot:
    def __init__(self, board):
        self.x = 0
        self.y = 0
        self.randomize_pos()
        self.acc_r = 0
        self.update_acc_r(board)

    def randomize_pos(self):
        self.x = randint(0, 7)
        self.y = randint(0, 3)

    def update_pos(self, x, y):
        self.x = x
        self.y = y

    def move(self, mov, board):
        if mov == "up":
            print("\tMoving up. ", end="")
            if self.y == 3:         # can't go up
                self.acc_r += -1                # edge collision cost
                print("Bump")
            else:
                self.update_pos(self.x, self.y + 1)
                self.acc_r += -0.1              # moving cost
                self.update_acc_r(board)        # add reinforcement according to what cell the robot is
                print()
        if mov == "right":
            print("\tMoving right. ", end="")
            if self.x == 7:
                self.acc_r += -1
                print("Bump")
            else:
                self.update_pos(self.x + 1, self.y)
                self.acc_r += -0.1
                self.update_acc_r(board)
                print()
        if mov == "down":
            print("\tMoving down. ", end="")
            if self.y == 0:
                self.acc_r += -1
                print("Bump")
            else:
                self.update_pos(self.x, self.y - 1)
                self.acc_r += -0.1
                self.update_acc_r(board)
                print()
        if mov == "left":
            print("\tMoving left. ", end="")
            if self.x == 0:
                self.acc_r += -1
                print("Bump")
            else:
                self.update_pos(self.x - 1, self.y)
                self.acc_r += -0.1
                self.update_acc_r(board)
                print()

    def update_acc_r(self, board):
        """ Looks at the board and updates reinforcement according to where the robot is """
        self.acc_r += board.board[self.x][self.y].content.r

    def __str__(self):
        return "Robot is on (" + str(self.x) + ", " + str(self.y) + "). Accumulated reinforcement: " + str(self.acc_r)
