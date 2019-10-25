from board import Board
from robot import Robot


def main():
    board = Board()
    board.print()
    robot = Robot()
    print(robot)
    
    # moving tests
    robot.move("up")
    print(robot)
    robot.move("up")
    print(robot)
    robot.move("left")
    print(robot)
    robot.move("down")
    print(robot)


if __name__ == "__main__":
    main()
