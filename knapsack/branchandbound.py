import numpy as np
from numpy import array

from Queue import Queue
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

def sortbydensity(w,p):
    w=array(w).astype(float)
    t=np.argsort(array(p)/array(w))[::-1]
    w1=[w[x] for x in t]
    p1=[p[x] for x in t]
    return w1, p1


def solveKnapsack(w, p, C):

    w,p=sortbydensity(w,p)

    #taken=[0]*len(w)

    n = len(w)
    maxBound=maxEstimate(w,p,C)
    #print maxBound
    #queue = Queue.Queue()
    #q=Queue()
    s=[]
    root=node(-1,0,0, maxBound,[])
    s.insert(0,root)
    maxProfit = 0
    #o=10
    bestList=[]

    while (s):
        t=[]
        v=s.pop(0)
        vLevel, vProfit, vWeight, vcontains = v.getLevel(), v.getValue(), v.getWeight(), v.getContains()
        ucontains=vcontains[:]

        if vLevel<n-1:
            uLevel = vLevel+1

        uProfit, uWeight, uBound = vProfit + p[uLevel], vWeight + w[uLevel], maxEstimate(w,p,C,uLevel, vProfit, vWeight)


        if (uWeight <= C):
            ucontains.append(uLevel)
            if (uProfit > maxProfit):
                maxProfit = uProfit
                bestList = ucontains

            if (uBound > maxProfit and uLevel<n-2):
                t.insert(0,node(uLevel, uProfit, uWeight,uBound, ucontains))


        uProfit = vProfit
        uWeight = vWeight
        if uLevel<n-2:
            uBound = maxEstimate(w,p,C,uLevel+1, vProfit, vWeight)


            if (uBound > maxProfit):
                    t.insert(0,node(uLevel, uProfit, uWeight,uBound, ucontains))


        for x in t:
            s.insert(0,x)




    taken = [0]*n
    for item in bestList:
        taken[item] = 1

    outputData = str(maxProfit) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, taken))
    return outputData


def maxEstimate(w,v,c,uLevel=0,uProfit=0, uWeight=0):
    v=array(v[uLevel:])
    w=array(w[uLevel:]).astype(float)
    #print v, w
    f=v/w
    order =np.argsort(f)[::-1]
    #print f, order
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



def getBound(uLevel, uProfit, uWeight, n, C, p, w):
    '''
    j = 0
    k = 0
    totalWeight = 0
    result = 0
    '''
    if (uWeight >= C):
        return 0
    else:
        result = uProfit
        totalWeight = uWeight
        j = uLevel + 1
        while j < n and (totalWeight + w[j]) <= C:
            result += p[j]#e[j][1]
            totalWeight = totalWeight + w[j]
            j += 1
        k = j
        if (k < n):
            result += (C - totalWeight) * p[k]/w[k]
        return result


v=[8,10,15,4]
w=[4,5,8,3]
c=11


#print "max " + str(maxEstimate(w,v,c, 1,0,0))


#nodes=[node(str(x), w[x], v[x]) for x in range(len(w))]
#print str(nodes[0])
#print sorted(v, key=lambda node: node.value/float(node.weight))

def solveit(file):
    inputDataFile = open(file, 'r')
    inputData = ''.join(inputDataFile.readlines())
    inputDataFile.close()
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


    print solveKnapsack(weights,values,capacity)

file = './data/ks_4_0'
solveit(file)