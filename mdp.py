def value_iteration(board, robot):
    moves = [0, 1, 2, 3]
    gama = 0.7

    for i in range(1000):         # For testing purposes
        # board.show_value_function()
        for x in range(8):
            for y in range(4):
                value_function_neighbor = []
                # Set the position of the robot
                robot.update_pos(x, y)
                print(robot)
                # Start the value iteration
                for move in moves:
                    value_function_neighbor.append(robot.try_move(move, board, gama, i))
                board.update_value_function(x, y, value_function_neighbor)
                # board.show_value_function()
    board.show_value_function()


def determine_policy(board):
    for y in range(4):
        for x in range(8):
            print("x =", x, "; y =", y, "arrow directions:", end=" ")
            neighbors_values = []
            neighbors = []
            if has_neighbor(x, y, 0):
                neighbors_values.append(board.get_value_function(x, y + 1))
                neighbors.append(0)
            if has_neighbor(x, y, 1):
                neighbors_values.append(board.get_value_function(x + 1, y))
                neighbors.append(1)
            if has_neighbor(x, y, 2):
                neighbors_values.append(board.get_value_function(x, y - 1))
                neighbors.append(2)
            if has_neighbor(x, y, 3):
                neighbors_values.append(board.get_value_function(x - 1, y))
                neighbors.append(3)
            best_option = min(neighbors_values)
            for idx, neighbor_value in enumerate(neighbors_values):
                if neighbor_value == best_option:
                    print(neighbors[idx], end=" ")
            print()


def has_neighbor(x, y, direction):
    if direction == 0 and y == 3:
        return False
    if direction == 1 and x == 7:
        return False
    if direction == 2 and y == 0:
        return False
    if direction == 3 and x == 0:
        return False
    return True
