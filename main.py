from board import Board
from robot import Robot


def main():
    board = Board()
    board.print()
    robot = Robot(board)
    print(robot)

    # moving tests
    robot.try_move(0, board)
    print(robot)
    robot.try_move(0, board)
    print(robot)
    robot.try_move(3, board)
    print(robot)
    robot.try_move(2, board)
    print(robot)


if __name__ == "__main__":
    main()
