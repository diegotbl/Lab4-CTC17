from random import randint


class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.randomize_pos()
        self.acc_r = 0

    def randomize_pos(self):
        self.x = randint(0, 7)
        self.y = randint(0, 3)

    def update_pos(self, x, y):
        self.x = x
        self.y = y

    def move(self, mov):
        if mov == "up":
            if self.y == 3:     # can't go up
                self.acc_r += -1        # edge collision cost
            else:
                self.update_pos(self.x, self.y + 1)
                self.acc_r += -0.1      # moving cost
        if mov == "right":
            if self.x == 7:
                self.acc_r += -1
            else:
                self.update_pos(self.x + 1, self.y)
                self.acc_r += -0.1
        if mov == "down":
            if self.y == 0:
                self.acc_r += -1
            else:
                self.update_pos(self.x, self.y - 1)
                self.acc_r += -0.1
        if mov == "left":
            if self.x == 0:
                self.acc_r += -1
            else:
                self.update_pos(self.x - 1, self.y)
                self.acc_r += -0.1

    def __str__(self):
        return "Robot is on (" + str(self.x) + ", " + str(self.y) + "). Accumulated reinforcement: " + str(self.acc_r)
