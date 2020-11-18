import numpy as np
import re

def insert_holidays(row):
    '''randomly inserts 7 days of holidays'''
    rest = [t.start() for t in re.finditer('10', row)] # find where working days end
    insert_to = np.random.choice(rest) + 1 # choose index to insert one week of holidays
    row = row[:insert_to] + '0'*7 + row[insert_to:]
    return row

def generate(I, D):
    S = np.zeros((I, D), dtype=int)
    for i in range(I):
        row = ''.join('1'*33 + '0'*23)*6 # Schedule without holidays
        for j in range(4):
            row = insert_holidays(row)

        # first_day = np.random.randint(0, self.D) # randomly select first day
        first_day = i*33 % 364 # first day shift for next worker
        row = row[first_day:] + row[:first_day] # permutate row to set first day

        S[i] = list(row) # add row to Schedule
    return S

def MAE(S, macines=8):
    needed = np.array([macines]*364)
    workers = S.sum(axis=0)
    error = np.abs(needed - workers).sum() / 364.
    return error
