import numpy as np
from GA.Schedule import Schedule
from GA.mutator import *
from GA.generator import mae, mae_flat

def solve(epochs = 200, mut_rounds = 20):
    # initial parents:
    parents = [Schedule(15), Schedule(15)]
    parents[0].give_birth()
    parents[1].give_birth()
    child = breed(parents)
    historic_child_MAEs = [1]*21

    solution_found = False

    # let evolution began!
    for epoch in range(epochs):
        #print info:
        print(f'Epoch {epoch + 1} of {epochs}. ', end='')
        print('Parental MAEs: %.2f %.2f. ' % (parents[0].mae(), parents[1].mae()), end='')
        print(f'Child MAE: %.2f\r' % (child.mae(),), end='')

        # Check if solution was found:
        if parents[0].is_solution():
            solution = parents[0]
            solution_found = True
            print('\nSolution found!')
            break
        elif parents[1].is_solution():
            solution = parents[1]
            solution_found = True
            print('\nSolution found!')
            break
        else:
            # create new child and check if it's better than previous:
            _child = breed(parents)
            for mut in range(mut_rounds):
                if _child.mae() < child.mae():
                    child = _child
                _child = mutate(_child)

        # child become parent if it's better than some of current parents:
        if (child.mae() <= parents[0].mae()) and (child.mae() != parents[0].mae()):
            parents[0] = child
        elif (child.mae() <= parents[1].mae()) and (child.mae() != parents[0].mae()):
            parents[1] = child
        else:
            new_parent = Schedule(15)
            new_parent.give_birth()
            for k in range(2):
                if parents[k].mae() > new_parent.mae():
                    parents[k] = new_parent

        historic_child_MAEs.append(child.mae())

        if historic_child_MAEs[-10:] == historic_child_MAEs[-11:-1]:
            for p_mut in range(mut_rounds//2):
                parents[0] = mutate(parents[0], p_mut % 15)
                parents[1] = mutate(parents[1], p_mut % 15)
            for c_mut in range(mut_rounds//10):
                child = mutate(breed(parents))

    if solution_found:
        return solution
    else:
        print('\nSolution is not found, you could try again using more epochs')
        return child, parents[0], parents[1], historic_child_MAEs
