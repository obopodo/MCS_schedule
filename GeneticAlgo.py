import numpy as np
from Schedule import Schedule

def breed(p1, p2):
    child = np.vstack((p1[:8, :], p2[8:, :]))
    return child

def mutate1(child):
    '''
    define mutation as permutation of last working and last resting days
    let insert mutation with the rate of 1/10
    '''
    m = np.random.randint(0,10)
    if m == 1:
        i = np.random.randint(0, child.shape(0)) # take random row
        row = np.array2string(child[0], separator='', max_line_width=370)[1:-1]
        rest = [t.start() for t in re.finditer('10', row)]
        r1, r0 = np.random.choice(rest, 2)
        row = list(row)
        row[r1], row[r0 + 1] = row[r0 + 1], row[r1]
        child[i] = row
