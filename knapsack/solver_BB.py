#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from numpy import array
from Queue import Queue
import numpy as np


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
    '''
    for i in range(0, items):
        if weight + weights[i] <= capacity:
            taken.append(1)
            value += values[i]
            weight += weights[i]
        else:
            taken.append(0)
    '''
    class node(object):
        def __init__(self, level, value, weight, bound, contains=[], ind=0):
            #self.name=str(name)
            self.weight=weight
            self.value=value
            self.level=level
            self.bound=bound
            self.contains=contains
            self.ind=ind
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
        def getIndex(self):
            return self.ind
        def __str__(self):
            return "(" + str(self.level) + " / " + str(self.value) + "/" + str(self.weight) + ")"


    w=weights
    v=values
    c=capacity

    def sortbydensity(items):
        items=sorted(items, key=lambda item: item[1]/float(item[0]), reverse=True)
        return items


    def solveKnapsack(wt, pr, C):
        items=[]
        for x in range(len(wt)):
            items.append((wt[x], pr[x], x))
        items=sortbydensity(items)

        maxW=0
        n = len(w)
        maxBound=maxEstimate(items,C)
        s=[]
        root=node(-1,0,0, maxBound,[],0)
        s.insert(0,root)
        maxProfit = 0
        bestList=[]


        while (s):
            t=[]
            v=s.pop(0)
            vLevel, vProfit, vWeight, vcontains = v.getLevel(), v.getValue(), v.getWeight(), v.getContains()
            ucontains=vcontains[:]

            if vLevel<n-1:
                uLevel = vLevel+1

            uProfit, uWeight, uBound = vProfit + items[uLevel][1], vWeight + items[uLevel][0], maxEstimate(items,C,uLevel, vProfit, vWeight)
            ucontains.append(items[uLevel][2])

            if (uWeight <= C):
                if (uProfit > maxProfit):
                    maxProfit = uProfit
                    bestList = ucontains

                if (uBound > maxProfit and uLevel<n-1):
                    t.insert(0,node(uLevel, uProfit, uWeight,uBound, ucontains, uLevel))
                if uWeight>maxW:
                    maxW=uWeight

            uProfit = vProfit
            uWeight = vWeight
            ucontains=vcontains[:]
            if uLevel<n-1:
                uBound = maxEstimate(items,C,uLevel+1, vProfit, vWeight)
                if (uBound > maxProfit):
                        t.insert(0,node(uLevel, uProfit, uWeight,uBound, ucontains, uLevel))


            for x in t:
                s.insert(0,x)


        taken = [0]*n
        for item in bestList:
            taken[item] = 1

        outputData = str(maxProfit) + ' ' + str(0) + '\n'
        outputData += ' '.join(map(str, taken))
        return outputData


    def maxEstimate(items,c,uLevel=0,uProfit=0, uWeight=0):
        tw=uWeight
        val=uProfit
        for item in items[uLevel:]:
                w=item[0]
                v=item[1]
                tw=tw+w
                val=val+v
                if tw>c:
                    tw=tw-w
                    val=val-v
                    dif=c-tw
                    frac=dif/float(w)
                    val+=frac*v
                    break
        return int(val)

    return solveKnapsack(weights,values,capacity)

import sys

if __name__ == '__main__':
    if len(sys.argv) ==1:
        inputDataFile = open('./data/ks_1000_0', 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solve_it(inputData)

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    #else:
        #print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'





