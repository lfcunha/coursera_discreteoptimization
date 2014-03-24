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


    '''
    for i in range(0, items):
        if weight + weights[i] <= capacity:
            taken.append(1)
            value += values[i]
            weight += weights[i]
        else:
            taken.append(0)
    '''
'''
    class node(object):
        def __init__(self, level, value, weight, bound, contains=[]):
            #self.name=str(name)
            self.weight=weight
            self.value=value
            self.level=level
            self.bound=bound
            self.contains=contains
        def getWeight(self):
            return self.weight
        def getValue(self):
            return self.value
        #def getName(self):
        #    return self.name
        def getLevel(self):
            return self.level
        def getBound(self):
            return self.bound
        def getContains(self):
            return self.contains
        def __str__(self):
            return "(" + str(self.level) + " / " + str(self.value) + "/" + str(self.weight) + ")"

    w=weights
    v=values
    c=capacity

    def sortbydensity(w,p):
        w=array(w).astype(float)
        t1=np.argsort(array(p)/array(w))[::-1]
        w1=[w[x] for x in t1]
        p1=[p[x] for x in t1]
        return w1, p1, t1


    def solveKnapsack(w, p, C):

        maxW=0
        #w,p,t1=sortbydensity(w,p)
        #print t1
        #taken=[0]*len(w)
        n = len(w)
        maxBound=maxEstimate(w,p,C)
        s=[]
        root=node(-1,0,0, maxBound,[])
        s.insert(0,root)
        maxProfit = 0
        bestList=[]
        #o=10

        while (s):
            #print bestList
            #print maxProfit
            t=[]
            v=s.pop(0)
            vLevel, vProfit, vWeight, vcontains = v.getLevel(), v.getValue(), v.getWeight(), v.getContains()
            ucontains=vcontains[:]



            if vLevel<n-1:
                uLevel = vLevel+1

            uProfit, uWeight, uBound = vProfit + p[uLevel], vWeight + w[uLevel], maxEstimate(w,p,C,uLevel, vProfit, vWeight)
            ucontains.append(uLevel)
            #bestList = ucontains

            if (uWeight <= C):

                if (uProfit > maxProfit):
                    maxProfit = uProfit
                    bestList = ucontains



                if (uBound > maxProfit and uLevel<n-1):
                    t.insert(0,node(uLevel, uProfit, uWeight,uBound, ucontains))
                if uWeight>maxW:
                    maxW=uWeight

            uProfit = vProfit
            uWeight = vWeight
            ucontains=vcontains[:]
            if uLevel<n-1:
                uBound = maxEstimate(w,p,C,uLevel+1, vProfit, vWeight)
                if (uBound > maxProfit):
                        t.insert(0,node(uLevel, uProfit, uWeight,uBound, ucontains))


            for x in t:
                s.insert(0,x)

            #print C, maxW


        taken = [0]*n
        taken2 = [0]*n
        #print "--"
        #print bestList
        for item in bestList:
            taken[item] = 1

        #taken2=[taken[x] for x in t1]

        outputData = str(maxProfit) + ' ' + str(0) + '\n'
        outputData += ' '.join(map(str, taken))
        return outputData
'''
'''
    def maxEstimate(w,v,c,uLevel=0,uProfit=0, uWeight=0):
        v=array(v[uLevel:])
        w=[float(x) for x in array(w[uLevel:])]
        f=v/w
        order =np.argsort(f)
        tw=uWeight
        val=uProfit
        for x in range(len(order)):
                tw=tw+w[order[x]]
                val=val+v[order[x]]
                if tw>c:
                    tw=tw-w[order[x]]
                    val=val-v[order[x]]
                    dif=c-tw
                    frac=dif/w[order[x]]
                    val+=frac*v[order[x]]
                    break
        return int(val)
'''

    #return solveKnapsack(weights,values,capacity)




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
