import numpy as np
from GA.Schedule import Schedule
from GA.mutator import *
from GA.generator import mae_flat

def solve(epochs=1000):
    his = []
    solution = Schedule(15)
    solution.give_birth()

    for i in range(epochs):
        print(f'Epoch {i} of {epochs}. MAE = {solution.mae()},\r', end='')
        new_solution = mutate(solution)
        if new_solution.mae() <= solution.mae():
            solution = new_solution
        his.append(solution.mae())

        if solution.is_solution():
            print('\nSolution is found!')
            break

    return solution, his
