import numpy as np
import re

def get_indexes(some_string, substring):
    indexes = np.array([s.start() for s in re.finditer(substring, some_string)])
    return indexes

def arr2str(arr):
    row = np.array2string(arr, separator='', max_line_width=370)[1:-1]
    return row

def mae(S, machines=8):
    needed = np.array([machines]*364)
    workers = S.sum(axis=0)
    error = np.abs(needed - workers).sum() / 364.
    return error

def mae_flat(coverage, machines=8):
    needed = np.array([machines]*364)
    error = np.abs(needed - coverage).sum() / 364.
    return error


def insert_holidays(row):
    '''randomly inserts 7 days of holidays'''
    rest = get_indexes(row, '10') # find where working days end
    insert_to = np.random.choice(rest) + 1 # choose index to insert one week of holidays
    row = row[:insert_to] + '0'*7 + row[insert_to:]
    return row

def generate(I, D):
    S = np.zeros((I, D), dtype=int)
    for i in range(I):
        row = ''.join('1'*33 + '0'*23)*6 # Schedule without holidays
        for j in range(4):
            row = insert_holidays(row)

        first_day = np.random.randint(0, D) # randomly select first day
        # first_day = i*33 % 364 # first day shift for next worker
        row = row[first_day:] + row[:first_day] # permutate row to set first day

        S[i] = list(row) # add row to Schedule
    return S
