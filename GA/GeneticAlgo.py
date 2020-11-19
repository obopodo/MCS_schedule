import numpy as np
from GA.Schedule import Schedule
from GA.mutator import *
from GA.generator import mae, mae_flat

def solve(epochs = 100, mut_rounds = 100):
    # initial parents:
    parents = [Schedule(15), Schedule(15)]
    parents[0].give_birth()
    parents[1].give_birth()
    child = breed(parents)

    solution_found = False

    # let evolution began!
    for epoch in range(epochs):
        print(f'Epoch {epoch} of {epochs}. ', end='')
        print('Parental MAEs: %.2f %.2f. ' % (parents[0].mae(), parents[1].mae()), end='')
        print(f'Child MAE: %.2f\r' % (child.mae(),), end='')

        if parents[0].is_solution():
            solution = parents[0]
            solution_found = True
            print('Solution found!')
            break
        elif parents[1].is_solution():
            solution = parents[1]
            solution_found = True
            print('Solution found!')
            break
        else:
            _child = breed(parents)
            for mut in range(mut_rounds):
                if _child.mae() < child.mae():
                    child = _child
                _child = mutate1(_child)

        if child.mae() <= parents[0].mae():
            parents[0] = child
        elif child.mae() <= parents[1].mae():
            parents[1] = child
        else:
            new_p = [Schedule(15), Schedule(15)]
            new_p[0].give_birth()
            new_p[0].give_birth()
            for k in range(2):
                for l in range(2):
                    if parents[k].mae() > new_p[l].mae():
                        parents[k] = new_p[l]

    if solution_found:
        return solution
    else:
        print('\nSolution is not found, you could try again using more epochs')
        return child, parents[0], parents[1]
