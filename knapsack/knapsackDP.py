__author__ = 'luiscunha'

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

    w=weights
    v=values
    c=capacity



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




    return DP(w,v,c)












if __name__ == '__main__':
       inputDataFile = open('./data/ks_4_0', 'r')
       inputData = ''.join(inputDataFile.readlines())
       inputDataFile.close()
       print solve_it(inputData)