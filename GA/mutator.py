import numpy as np
from .Schedule import Schedule
from  .generator import *


def breed(parents, i=8, simple_split=False):
    child = Schedule(parents[0].I)
    if simple_split:
        chromo = np.random.permutation([0 ,1]) # select two parental chromosomes randomly
        child.S = np.vstack((parents[chromo[0]].S[:i, :], parents[chromo[1]].S[i:, :]))
        child.update_coverage()
    else:
        all_ch = np.arange(parents[0].I)
        # select random subset of parental rows
        chromo1 = np.random.choice(all_ch, 8, replace=False)
        chromo2 = list(set(all_ch) - set(chromo1))
        child.S = np.vstack((parents[0].S[chromo1], parents[1].S[chromo2]))
        child.update_coverage()
    return child

def mutate(child, i = False):
    '''
    Define mutation2 as permutation of last working and first resting days
    and vice versa.
    Mutation occurs if the day with '1' contains >8 workers and the day with '0' <8
    '''
    # _child = Schedule(child.I)
    # _child.S = child.S.copy()
    # _child.update_coverage()

    _child = child.copy()

    if not i:
        i = np.random.randint(0, child.I) # take random row if not specified

    row = arr2str(child.S[i])
    rest_starts = get_indexes(row, '10') # get indexes of transitions between work and rest
    work_starts = get_indexes(row, '01')

    # boundary days:
    ones_indexes = np.append(rest_starts, work_starts + 1)
    zeros_indexes = np.append(work_starts, rest_starts + 1)
    cover_ones = child.coverage[ones_indexes]
    cover_zeros = child.coverage[zeros_indexes]

    max_ones = np.argmax(cover_ones) # this day has maximal coverage and the row has 1 here
    min_ones = np.argmin(cover_zeros) # this day has minimal coverage and the row has 0 here

    max_day = ones_indexes[max_ones]
    min_day = zeros_indexes[min_ones]
    row = list(row)
    row[max_day], row[min_day] = row[min_day], row[max_day] # switch 1 and 0
    _child.S[i] = row
    _child.update_coverage()
    return _child
