import numpy as np
import re
from .Helping_methods import generate, MAE

class Schedule():
    def __init__(self, I):
        self.I = I
        self.D = (33+23)*6 + 28
        self.S = np.zeros((self.I, self.D), dtype=int)

    def give_birth(self):
        converged = False
        best_solution = generate(self.I, self.D)
        max_iter = 200

        for j in range(max_iter):
            error_best = MAE(best_solution)
            if np.all(round(error_best) == 0.):
                converged = True
                break

            new_solution = generate(self.I, self.D)
            error_new = MAE(new_solution)

            if error_new < error_best:
                best_solution = new_solution

        self.S = best_solution
