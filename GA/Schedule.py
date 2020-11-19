import numpy as np
import re
from .generator import generate, mae, mae_flat

class baby():
    def __init__(self, I, D):
        self.I = I
        self.D = D
        self.S = np.zeros((self.I, self.D), dtype=int)
        self.coverage = np.zeros(self.D)

    def update_coverage(self):
        self.coverage = self.S.sum(axis=0)

    def __repr__(self):
        return np.array2string(self.S)

class Schedule():
    def __init__(self, I):
        self.I = I
        self.D = (33+23)*6 + 28
        self.S = np.zeros((self.I, self.D), dtype=int)
        self.coverage = np.zeros(self.D)

    def update_coverage(self):
        self.coverage = self.S.sum(axis=0)

    def is_solution(self):
        return np.all(self.coverage == [8] * self.D)

    def mae(self):
        return mae_flat(self.coverage)

    def give_birth(self):
        converged = False
        best_solution = generate(self.I, self.D)
        max_iter = 200

        for j in range(max_iter):
            error_best = mae(best_solution)
            if np.all(round(error_best) == 0.):
                converged = True
                break

            new_solution = generate(self.I, self.D)
            error_new = mae(new_solution)

            if error_new < error_best:
                best_solution = new_solution

        self.S = best_solution
        self.update_coverage()

    def __repr__(self):
        return np.array2string(self.S)
