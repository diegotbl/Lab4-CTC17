from board import Board
from robot import Robot


def main():
    board = Board()
    board.print()
    robot = Robot(board)
    print(robot)

    # moving tests
    robot.move("up", board)
    print(robot)
    robot.move("up", board)
    print(robot)
    robot.move("left", board)
    print(robot)
    robot.move("down", board)
    print(robot)


if __name__ == "__main__":
    main()
