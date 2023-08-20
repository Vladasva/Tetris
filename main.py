import numpy as np
from collections import deque
from Figure import Figures
from Move import Move
from Printer import Printer
def controller(transformed, bottom_row, left_column, right_column, output):
    moves_counter = 0
    check_counter = 0

    flag_1 = True
    while flag_1:

        movement = input()

        if movement.lower() == "rotate":
            transformed = transformed.astype(int)
            movement_ahead = transformed + 10
            movement_ahead = movement_ahead.astype(str)
            if np.isin(movement_ahead, concatenated_list).any():
                transformed = movements[0]
                game.appendleft(transformed)
                check_counter += 1
                if check_counter == 1:
                    flag_1 = False
            else:
                if np.isin(bottom_row, movements[0]).any():
                    transformed = movements[0]
                    game.appendleft(transformed)
                    check_counter += 1
                    if check_counter == 1:
                        flag_1 = False
                elif np.isin(left_column, movements[0]).any() or np.isin(right_column, movements[0]).any():
                    substring = movements[0]
                    moves_counter += 10
                    transformed = Move.move_down(substring, figure_obj, moves_counter)
                    transformed = transformed.astype(str)
                    if np.isin(bottom_row, movements[0]).any():
                        transformed = movements[0]
                        game.appendleft(transformed)
                        check_counter += 1
                        if check_counter == 1:
                            flag_1 = False
                else:
                    substring = movements[0]
                    moves_counter += 10
                    transformed = Move.rotate_figure(substring, figure_obj, moves_counter)
                    transformed = transformed.astype(str)

        elif movement.lower() == "left":
            transformed_1 = transformed.astype(int)
            movement_ahead = transformed_1 + 10
            movement_ahead = movement_ahead.astype(str)
            if np.isin(movement_ahead, concatenated_list).any():
                transformed = movements[0]
                game.appendleft(transformed)
                check_counter += 1
                if check_counter == 1:
                    flag_1 = False
            else:
                if np.isin(bottom_row, movements[0]).any():
                    transformed = movements[0]
                    game.appendleft(transformed)
                    check_counter += 1
                    if check_counter == 1:
                        flag_1 = False
                elif np.isin(left_column, movements[0]).any():
                    substring = movements[0]
                    moves_counter += 10
                    transformed = Move.move_down(substring, figure_obj, moves_counter)
                    transformed = transformed.astype(str)
                    if np.isin(bottom_row, movements[0]).any():
                        transformed = movements[0]
                        game.appendleft(transformed)
                        check_counter += 1
                        if check_counter == 1:
                            flag_1 = False
                else:
                    if len(movements) == 1:
                        substring = movements[0]
                        moves_counter += 10
                        moves_counter -= 1
                        transformed = Move.move_left(substring, figure_obj, moves_counter)
                        transformed = transformed.astype(str)
                    elif len(movements) > 0:
                        transformed_2 = transformed.astype(int)
                        movement_ahead_1 = transformed_2 - 2
                        movement_ahead_1 = movement_ahead_1.astype(str)
                        if np.isin(movement_ahead_1, concatenated_list).any():
                            substring = movements[0]
                            moves_counter -= 1
                            transformed_4 = Move.move_left(substring, figure_obj, moves_counter)
                            transformed = transformed_4.astype(str)
                        else:
                            substring = movements[0]
                            moves_counter += 10
                            moves_counter -= 1
                            transformed = Move.move_left(substring, figure_obj, moves_counter)
                            transformed = transformed.astype(str)

        elif movement.lower() == "right":
            transformed = transformed.astype(int)
            movement_ahead = transformed + 10
            movement_ahead = movement_ahead.astype(str)
            if np.isin(movement_ahead, concatenated_list).any():
                transformed = movements[0]
                game.appendleft(transformed)
                check_counter += 1
                if check_counter == 1:
                    flag_1 = False
            else:
                if np.isin(bottom_row, movements[0]).any():
                    transformed = movements[0]
                    game.appendleft(transformed)
                    check_counter += 1
                    if check_counter == 1:
                        flag_1 = False
                elif np.isin(right_column, movements[0]).any():
                    substring = movements[0]
                    moves_counter += 10
                    transformed = Move.move_down(substring, figure_obj, moves_counter)
                    transformed = transformed.astype(str)
                    if np.isin(bottom_row, movements[0]).any():
                        transformed = movements[0]
                        game.appendleft(transformed)
                        check_counter += 1
                        if check_counter == 1:
                            flag_1 = False
                else:
                    if len(movements) == 1:
                        substring = movements[0]
                        moves_counter += 10
                        moves_counter += 1
                        transformed = Move.move_right(substring, figure_obj, moves_counter)
                        transformed = transformed.astype(str)
                    elif len(movements) > 0:
                        transformed_5 = transformed.astype(int)
                        movement_ahead_2 = transformed_5 + 1
                        movement_ahead_2 = movement_ahead_2.astype(str)
                        if np.isin(movement_ahead_2, concatenated_list).any():
                            substring = movements[0]
                            moves_counter += 1
                            transformed_5 = Move.move_right(substring, figure_obj, moves_counter)
                            transformed = transformed_5.astype(str)
                        else:
                            substring = movements[0]
                            moves_counter += 10
                            moves_counter += 1
                            transformed = Move.move_right(substring, figure_obj, moves_counter)
                            transformed = transformed.astype(str)

        elif movement.lower() == "down":
            transformed_6 = transformed.astype(int)
            movement_ahead_3 = transformed_6 + 10
            movement_ahead_3 = movement_ahead_3.astype(str)
            if np.isin(movement_ahead_3, concatenated_list).any():
                transformed = movements[0]
                game.appendleft(transformed)
                check_counter += 1
                if check_counter == 1:
                    flag_1 = False
            else:
                if np.isin(bottom_row, movements[0]).any():
                    transformed = movements[0]
                    game.appendleft(transformed)
                    check_counter += 1
                    if check_counter >= 1:
                        flag_1 = False
                else:
                    if len(movements) == 1:
                        substring = movements[0]
                        moves_counter += 10
                        transformed = Move.move_down(substring, figure_obj, moves_counter)
                        transformed = transformed.astype(str)
                    elif len(movements) > 0:
                        substring = movements[0]
                        moves_counter += 10
                        transformed = Move.move_down(substring, figure_obj, moves_counter)
                        transformed = transformed.astype(str)
                        movements.appendleft(transformed)

        elif movement.lower() == "exit":
            flag_1 = False
            return flag_1

        Printer.matrix_not_empty(transformed, concatenated_list, height, width, movement_counter)

        movements.appendleft(transformed)

    output = output.astype(str)

    for col in range(output.shape[1]):
        if np.all(output[:, col] == "0"):
            print("Game Over!")
            flag = False
            return flag


size = input()
width, height = size.split()

movements = deque()

game = deque()

matrix_1 = Printer.print_empty_matrix(height, width)

movement_counter = 0

concatenated_list = []

flag = True

while flag:

    action = input()

    if action == "piece":
        figure = input()

        figure_obj = Figures.return_figures(figure)

        movements.appendleft(figure_obj[0])

        transformed = figure_obj[0]

        if len(game) > 0:
            for lst in game:
                concatenated_list.extend(lst)

        matrix = Printer.provide_matrix(height, width)

        output = Printer.matrix_not_empty(transformed, concatenated_list, height, width, movement_counter)

        # Select the boundary rows and columns
        bottom_row = matrix[-1, :]
        left_column = matrix[1:-1, 0]
        right_column = matrix[1:-1, -1]

        result = controller(transformed, bottom_row, left_column, right_column, output)

        concatenated_list = []

        if len(game) > 0:
            for lst in game:
                concatenated_list.extend(lst)

        if result == False:
            flag = False

        movement_counter += 1

    elif action.lower() == "exit":
        flag = False
    elif action == "break":
        matrix_check = np.zeros((int(height), int(width)))

        # Initialize a counter variable to keep track of the current number
        counter = 0

        # Iterate over each element of the matrix and assign sequential numbers
        for i in range(matrix_check.shape[0]):
            for j in range(matrix_check.shape[1]):
                matrix_check[i, j] = counter
                counter += 1

        matrix_check = matrix_check.astype(int)
        matrix_check = matrix_check.astype(str)

        deleted_rows = 0

        for row in matrix_check:
            if all(x in concatenated_list for x in row):
                concatenated_list = [x for x in concatenated_list if x not in row]
                deleted_rows += 1

        concatenated_list_int = [int(i) for i in concatenated_list]
        concatenated_list_int = [i + (10 * deleted_rows) for i in concatenated_list_int]
        concatenated_list = [str(i) for i in concatenated_list_int]

        output = Printer.matrix_after_break(concatenated_list, height, width)

        game.clear()

        game.appendleft(concatenated_list)