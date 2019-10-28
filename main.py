from board import Board
from robot import Robot
from mdp import value_iteration


def main():
    board = Board()
    board.print()
    robot = Robot(board)
    print(robot)

    value_iteration(board, robot)


if __name__ == "__main__":
    main()
