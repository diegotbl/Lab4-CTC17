from board import Board
from robot import Robot
from mdp import value_iteration, determine_policy


def main():
    board = Board()
    board.print()
    robot = Robot(board)

    value_iteration(board, robot)
    determine_policy(board)


if __name__ == "__main__":
    main()
