def value_iteration(board, robot):
    moves = [0, 1, 2, 3]

    # while True:
    for i in range(2):         # For testing purposes
        board.show_value_funtion()
        for x in range(8):
            for y in range(4):
                value_function_neighbor = []
                # Set the positon of the robot
                robot.update_pos(x, y)
                print(robot)
                # Start the value iteration
                for move in moves:
                    value_function_neighbor.append(robot.try_move(move, board))
                board.update_value_function(x, y, value_function_neighbor)
                board.show_value_funtion()