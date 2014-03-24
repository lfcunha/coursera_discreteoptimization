#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
    capacity = int(firstLine[1])

    values = []
    weights = []

    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    items = len(values)

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    '''
    for i in range(0, items):
        if weight + weights[i] <= capacity:
            taken.append(1)
            value += values[i]
            weight += weights[i]
        else:
            taken.append(0)
    '''
    w=weights
    v=values
    c=capacity
    def knapsack(w, v, c):                           # Returns solution matrices
        n = len(w)                                   # Number of available items
        m = [[0]*(c+1) for i in range(n+1)]          # Empty max-value matrix
        P = [[False]*(c+1) for i in range(n+1)]      # Empty keep/drop matrix
        for k in range(1,n+1):                       # We can use k first objects
            i = k-1                                  # Object under consideration
            for r in range(1,c+1):                   # Every positive capacity
                m[k][r] = drop = m[k-1][r]           # By default: drop the object
                if w[i] > r: continue               # Too heavy? Ignore it
                keep = v[i] + m[k-1][r-w[i]]         # Value of keeping it
                m[k][r] = max(drop, keep)            # Best of dropping and keeping
                P[k][r] = keep > drop               # Did we keep it?
        return m, P


    m, P = knapsack(w, v, c)
    k, r, items = len(w), c, set()
    while k > 0 and r > 0:
       i = k-1
       if P[k][r]:
           items.add(i)
           r -= w[i]
       k -= 1
    #print items
    #print k,r

    taken=[]
    for i in range(len(v)):
        if i in items:
            taken.append(1)
        else:
            taken.append(0)

    value=0
    for i in range(len(taken)):
        value=value+taken[i]*w[i]

    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, taken))
    return outputData


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solve_it(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

