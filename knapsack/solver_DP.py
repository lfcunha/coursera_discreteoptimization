#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from numpy import array
from Queue import Queue
import numpy as np

from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from numpy.linalg import solve, norm
from numpy.random import rand



Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(inputData):
    #print inputData
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

    def DP(w,v,c):
        #print w,v,c
        n=len(w)
        table = lil_matrix((c+1, n+1))
        for i in range(1,n+1):
            wt, val = w[i-1], v[i-1]
            for wgt in range(1,c+1):
                if wt>wgt:
                    #print x
                    table[wgt,i] = table[wgt,i-1]
                else:
                    #print x
                    table[wgt,i] = max(table[wgt, i-1], table[wgt-wt,i-1] + val)
                #print table[wgt,i]
        #print table

        path=[]
        i=c
        j=len(w)
        while(j>0):
            if table[i, j-1] == table[i,j]:
                  j-=1
            else:
                path.append(j)
                i=i-w[j-1]
                j-=1

        taken=[0]*len(w)
        for x in path:
            taken[x-1]=1
        #print taken

        outputData = str(int(table[c,len(w)])) + ' ' + str(0) + '\n'
        outputData += ' '.join(map(str, taken))

        return outputData


    return DP(weights,values,capacity)



import sys

if __name__ == '__main__':
       #inputDataFile = open('./data/ks_19_0', 'r')
       #inputData = ''.join(inputDataFile.readlines())
       #inputDataFile.close()
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'
__author__ = 'luiscunha'
