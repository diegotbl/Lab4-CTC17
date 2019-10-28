def value_iteration(board, robot):
    # moving tests
    robot.try_move(0, board)
    print(robot)
    robot.try_move(0, board)
    print(robot)
    robot.try_move(3, board)
    print(robot)
    robot.try_move(2, board)
    print(robot)

    # while True:
    for i in range(10):         # For testing purposes
        pass
