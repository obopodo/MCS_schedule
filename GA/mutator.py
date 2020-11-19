import numpy as np
from .Schedule import Schedule
from  .generator import *


def breed(parents, i=8):
    child = Schedule(parents[0].I)
    chromo = np.random.permutation([0 ,1]) # select chromosomes randomly
    child.S = np.vstack((parents[chromo[0]].S[:i, :], parents[chromo[1]].S[i:, :]))
    child.update_coverage()
    return child

def mutate1(child):
    '''
    define mutation1 as permutation of last working and last resting days
    let insert mutation with the rate of 1/10
    '''
    _child = Schedule(child.I)
    _child.S = child.S.copy()
    _child.update_coverage()

    i = np.random.randint(0, child.I) # take random row
    row = arr2str(child.S[0])
    rest = get_indexes(row, '10')
    work = get_indexes(row, '01')
    r = np.random.choice(rest)
    w = np.random.choice(work)
    row = list(row)
    row[r], row[w] = row[w], row[r]
    _child.S[i] = row
    _child.update_coverage()
    return _child


def mutate2(child):
    '''
    Define mutation2 as permutation of last working and first resting days
    and vice versa.
    Mutation occurs if the day with '1' contains >8 workers and the day with '0' <8
    '''
    _child = Schedule(child.I)
    _child.S = child.S.copy()
    _child.update_coverage()

    i = np.random.randint(0, child.I) # take random row
    row = arr2str(child.S[i])
    rest_starts = get_indexes(row, '10') # get indexes of transitions between work and rest
    work_starts = get_indexes(row, '01')

    '''get boundary days coverage with workers '''
    row_ones_last = child.coverage[rest_starts]
    row_zeros_last = child.coverage[work_starts]
    row_ones_first = child.coverage[work_starts + 1]
    row_zeros_first = child.coverage[rest_starts + 1]

    switch_first = np.random.choice([True, False]) # choose strategy

    if switch_first:
        max_ones = np.argmax(row_ones_first)
        min_ones = np.argmin(row_zeros_first)
    else:
        max_ones = np.argmax(row_ones_last)
        min_ones = np.argmin(row_zeros_last)

    row = list(row)
    row[max_ones], row[min_ones] = row[min_ones], row[max_ones] # switch 1 and 0
    _child.S[i] = row
    _child.update_coverage()
    return _child

def mutate3(child):
    '''
    Define mutation2 as permutation of last working and first resting days
    and vice versa.
    Mutation occurs if the day with '1' contains >8 workers and the day with '0' <8
    '''
    _child = Schedule(child.I)
    _child.S = child.S.copy()
    _child.update_coverage()

    i = np.random.randint(0, child.I) # take random row
    row = arr2str(child.S[i])
    rest_starts = get_indexes(row, '10') # get indexes of transitions between work and rest
    work_starts = get_indexes(row, '01')

    '''get boundary days coverage with workers '''
    row_ones_last = child.coverage[rest_starts]
    row_zeros_last = child.coverage[work_starts]
    row_ones_first = child.coverage[work_starts + 1]
    row_zeros_first = child.coverage[rest_starts + 1]

    switch_first = np.random.choice([True, False]) # choose strategy

    if switch_first:
        max_ones = np.random.choice(row_ones_first)
        min_ones = np.random.choice(row_zeros_first)
    else:
        max_ones = np.random.choice(row_ones_last)
        min_ones = np.random.choice(row_zeros_last)

    row = list(row)
    row[max_ones], row[min_ones] = row[min_ones], row[max_ones] # switch 1 and 0
    _child.S[i] = row
    _child.update_coverage
    return _child
