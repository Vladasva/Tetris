import numpy as np
class Figures:
    def __init__(self, name):
        self.name = name
    @staticmethod
    def return_figures(figure):
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