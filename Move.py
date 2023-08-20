import numpy as np
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