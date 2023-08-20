import numpy as np
from collections import deque


class Figures:
    def __init__(self, figure):
        self.figure = figure

    @staticmethod
    def return_figures():
        if figure.upper() == "O":
            return np.array([[4, 14, 15, 5]]).astype(str)
        elif figure.upper() == "I":
            return np.array([[4, 14, 24, 34], [3, 4, 5, 6]]).astype(str)
        elif figure.upper() == "S":
            return np.array([[5, 4, 14, 13], [4, 14, 15, 25]]).astype(str)
        elif figure.upper() == "Z":
            return np.array([[4, 5, 15, 16], [5, 15, 14, 24]]).astype(str)
        elif figure.upper() == "L":
            return np.array([[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]).astype(str)
        elif figure.upper() == "J":
            return np.array([[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]).astype(str)
        elif figure.upper() == "T":
            return np.array([[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]).astype(str)


class Move:
    def __init__(self, substring, figure_obj, moves_counter):
        self.substring = substring
        self.figure_obj = figure_obj
        self.moves_counter = moves_counter

    @staticmethod
    def rotate_figure(substring, figure_obj, moves_counter):
        if len(figure_obj) == 4:
            if np.array_equal(substring, figure_obj[0]):
                substring = figure_obj[1].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter - 10
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[1]):
                substring = figure_obj[2].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[2]):
                substring = figure_obj[3].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[3]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[3]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[1].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            return substring
        elif len(figure_obj) == 2:
            if np.array_equal(substring, figure_obj[0]):
                substring = figure_obj[1].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter - 10
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[1]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[1].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            return substring
        elif len(figure_obj) == 1:
            if np.array_equal(substring, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter - 10
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            return substring

    @staticmethod
    def move_right(substring, figure_obj, moves_counter):
        if len(figure_obj) == 4:
            if np.array_equal(substring, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter - 10 - 1
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[1]):
                substring = figure_obj[1].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[2]):
                substring = figure_obj[2].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[3]):
                substring = figure_obj[3].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter - 1
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[1]):
                substring = figure_obj[1].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[2]):
                substring = figure_obj[2].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[3]):
                substring = figure_obj[3].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            return substring

        elif len(figure_obj) == 2:
            if np.array_equal(substring, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter - 10 - 1
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[1]):
                substring = figure_obj[1].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter - 1
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[1]):
                substring = figure_obj[1].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            return substring

        elif len(figure_obj) == 1:
            if np.array_equal(substring, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter - 10 - 1
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter - 1
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            return substring

    @staticmethod
    def move_left(substring, figure_obj, moves_counter):
        if len(figure_obj) == 4:
            if np.array_equal(substring, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter - 10 + 1
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[1]):
                substring = figure_obj[1].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[2]):
                substring = figure_obj[2].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[3]):
                substring = figure_obj[3].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter + 1
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[1]):
                substring = figure_obj[1].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[2]):
                substring = figure_obj[2].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[3]):
                substring = figure_obj[3].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[3]):
                substring = figure_obj[3].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            return substring

        elif len(figure_obj) == 2:
            if np.array_equal(substring, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter - 10 + 1
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[1]):
                substring = figure_obj[1].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter + 1
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[1]):
                substring = figure_obj[1].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            return substring

        elif len(figure_obj) == 1:
            if np.array_equal(substring, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter - 10 + 1
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter + 1
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            return substring
        return substring

    @staticmethod
    def move_down(substring, figure_obj, moves_counter):
        if len(figure_obj) == 4:
            if np.array_equal(substring, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter - 10
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[1]):
                substring = figure_obj[1].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[2]):
                substring = figure_obj[2].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[3]):
                substring = figure_obj[3].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            return substring

        elif len(figure_obj) == 2:
            if np.array_equal(substring, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter - 10
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[1]):
                substring = figure_obj[1].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            elif np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            return substring

        elif len(figure_obj) == 1:
            if np.array_equal(substring, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring

            substring = substring.astype(int)
            previous_counter = moves_counter - 10
            substring_1 = substring - previous_counter
            substring_1 = substring_1.astype(str)

            if np.array_equal(substring_1, figure_obj[0]):
                substring = figure_obj[0].astype(int)
                substring = substring + moves_counter
                substring = substring.astype(str)
                return substring
            return substring

        return substring


class Printer:
    def __init__(self):
        self.height = height
        self.width = width

    @staticmethod
    def print_empty_matrix(height, width):
        matrix = np.empty((int(height), int(width)), dtype=str)

        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                matrix[i, j] = "-"

        for row in matrix:
            print(' '.join(row))
        print()

        return matrix

    @staticmethod
    def provide_matrix(height, width):
        # Create a NumPy matrix of size 10x20 filled with zeros
        matrix = np.zeros((int(height), int(width)))

        # Initialize a counter variable to keep track of the current number
        counter = 0

        # Iterate over each element of the matrix and assign sequential numbers
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                matrix[i, j] = counter
                counter += 1

        matrix = matrix.astype(int)
        matrix = matrix.astype(str)

        return matrix

    @staticmethod
    def matrix_not_empty(transformed, concatenated_list):
        # Create a NumPy matrix of size 10x20 filled with zeros
        matrix = np.zeros((int(height), int(width)))

        # Initialize a counter variable to keep track of the current number
        counter = 0

        # Iterate over each element of the matrix and assign sequential numbers
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                matrix[i, j] = counter
                counter += 1

        matrix = matrix.astype(int)
        matrix = matrix.astype(str)

        output = np.empty_like(matrix, dtype=str)  # Create an empty output matrix

        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i, j] in transformed:
                    output[i, j] = "0"
                else:
                    output[i, j] = "-"

        if movement_counter > 0:

            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    if matrix[i, j] in concatenated_list:
                        output[i, j] = "0"
                    else:
                        pass

        for row in output:
            print(' '.join(row))
        print()

        return output

    @staticmethod
    def matrix_after_break(concatenated_list):
        # Create a NumPy matrix of size 10x20 filled with zeros
        matrix_n = np.zeros((int(height), int(width)))

        # Initialize a counter variable to keep track of the current number
        counter = 0

        # Iterate over each element of the matrix and assign sequential numbers
        for i in range(matrix_n.shape[0]):
            for j in range(matrix_n.shape[1]):
                matrix_n[i, j] = counter
                counter += 1

        matrix_n = matrix_n.astype(int)
        matrix_n = matrix_n.astype(str)

        output = np.empty_like(matrix_n, dtype=str)  # Create an empty output matrix

        for i in range(matrix_n.shape[0]):
            for j in range(matrix_n.shape[1]):
                if str(matrix_n[i, j]) in concatenated_list:
                    output[i, j] = "0"
                else:
                    output[i, j] = "-"

        for row in output:
            print(' '.join(row))
        print()

        return output


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
                    print("test 1")
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

        elif movement.lower() == "exit":
            flag_1 = False
            return flag_1

        Printer.matrix_not_empty(transformed, concatenated_list)

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

        figure_obj = Figures(figure)

        figure_obj = figure_obj.return_figures()

        movements.appendleft(figure_obj[0])

        transformed = figure_obj[0]

        if len(game) > 0:
            for lst in game:
                concatenated_list.extend(lst)

        matrix = Printer.provide_matrix(height, width)

        output = Printer.matrix_not_empty(transformed, concatenated_list)

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

        print(concatenated_list)

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

        output = Printer.matrix_after_break(concatenated_list)

        game.clear()

        game.appendleft(concatenated_list)










