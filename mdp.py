def show_value_function(board):
    for y in [3, 2, 1, 0]:
        for x in range(8):
            print(board.get_value_function(x, y), end="\t")
        print()
    print()

def value_iteration(board, robot):
    moves = [0, 1, 2, 3]
    # moving tests
    #robot.try_move(0, board)
    #print(robot)
    #robot.try_move(1, board)
    #print(robot)
    #robot.try_move(3, board)
    #print(robot)
    #robot.try_move(2, board)
    #print(robot)

    # while True:
    for i in range(2):         # For testing purposes
        for x in range(8):
            for y in range(4):
                value_function_neighbor = []
                # Set the positon of the robot
                robot.set_position(x, y)
                # Start the value iteration
                for move in moves:
                    value_function_neighbor.append(robot.try_move(move, board))
                board.update_value_function(x, y, value_function_neighbor)
                show_value_function(board)