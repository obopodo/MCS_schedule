import numpy as np
from GA.Schedule import Schedule
from GA.mutator import *

def solve(epochs=1000):
    his = [] # history logging
    solution = Schedule(15)
    solution.give_birth()

    for i in range(epochs):
        print(f'Epoch {i} of {epochs}. MAE = {solution.mae()},\r', end='')
        new_solution = mutate(solution)

        # this loop checks for corrupted rows
        # they arise sometimes IDK why. Some mistake in muator, but I can't find it
        corrupted = False
        for r in new_solution.S:
            row = arr2str(r)
            badind = [get_indexes(row, '101'), get_indexes(row, '010')]
            for b in badind:
                if len(b) != 0:
                    corrupted = True
                    print('\ncorrupted!')
                    break
                else:
                    continue
                break

        # update solution:
        if (new_solution.mae() <= solution.mae()) and not corrupted:
            solution = new_solution
        his.append(solution.mae())

        if solution.is_solution():
            print('\nSolution is found!')
            break

    return solution, his
