import numpy as np
class Printer:
    def __init__(self, name):
        self.name = name

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
    def matrix_not_empty(transformed, concatenated_list, height, width, movement_counter):
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
    def matrix_after_break(concatenated_list, height, width):
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
