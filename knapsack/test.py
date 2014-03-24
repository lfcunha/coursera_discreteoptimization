import Queue

#w is a list of items' weights and p their corresponding profits
#C is the size of the knapsack
def solveKnapsack(w, p, C):
    n = len(w)
    queue = Queue.Queue()

    vLevel = -1
    vProfit = 0
    vWeight = 0

    queue.put(vLevel)
    queue.put(vProfit)
    queue.put(vWeight)
    maxProfit = 0
    bound = 0
    while (not queue.empty()):
        vLevel = queue.get()
        vProfit = queue.get()
        vWeight = queue.get()

        uLevel = vLevel
        if (vLevel == -1):
            uLevel = 0
        elif (vLevel != (n - 1)):
            uLevel = vLevel + 1
        uProfit = vProfit + p[uLevel]
        uWeight = vWeight + w[uLevel]
        bound = getBound(uLevel, uProfit, uWeight, n, C, p, w)

        if (uWeight <= C and uProfit > maxProfit):
            maxProfit = uProfit

        if (bound > maxProfit):
            queue.put(uLevel)
            queue.put(uProfit)
            queue.put(uWeight)

        uProfit = vProfit
        uWeight = vWeight
        bound = getBound(uLevel, uProfit, uWeight, n, C, p, w)

        if (bound > maxProfit):
            queue.put(uLevel)
            queue.put(uProfit)
            queue.put(uWeight)
    return maxProfit

def getBound(uLevel, uProfit, uWeight, n, C, p, w):
    j = 0
    k = 0
    totalWeight = 0
    result = 0

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

v=[90000, 89750, 10001, 89500, 10252, 89250, 10503, 89000, 10754, 88750, 11005, 88500, 11256, 88250, 11507, 88000, 11758, 87750, 12009, 87500, 12260, 87250, 12511, 87000, 12762, 86750, 13013, 86500, 13264, 86250, 13515, 86000, 13766, 85750, 14017, 85500, 14268, 85250, 14519, 85000, 14770, 84750, 15021, 84500, 15272, 84250, 15523, 84000, 15774, 83750, 16025, 83500, 16276, 83250, 16527, 83000, 16778, 82750, 17029, 82500, 17280, 82250, 17531, 82000, 17782, 81750, 18033, 81500, 18284, 81250, 18535, 81000, 18786, 80750, 19037, 80500, 19288, 80250, 19539, 80000, 19790, 79750, 20041, 79500, 20292, 79250, 20543, 79000, 20794, 78750, 21045, 78500, 21296, 78250, 21547, 78000, 21798, 77750, 22049, 77500]
w=[90001, 89751, 10002, 89501, 10254, 89251, 10506, 89001, 10758, 88751, 11010, 88501, 11262, 88251, 11514, 88001, 11766, 87751, 12018, 87501, 12270, 87251, 12522, 87001, 12774, 86751, 13026, 86501, 13278, 86251, 13530, 86001, 13782, 85751, 14034, 85501, 14286, 85251, 14538, 85001, 14790, 84751, 15042, 84501, 15294, 84251, 15546, 84001, 15798, 83751, 16050, 83501, 16302, 83251, 16554, 83001, 16806, 82751, 17058, 82501, 17310, 82251, 17562, 82001, 17814, 81751, 18066, 81501, 18318, 81251, 18570, 81001, 18822, 80751, 19074, 80501, 19326, 80251, 19578, 80001, 19830, 79751, 20082, 79501, 20334, 79251, 20586, 79001, 20838, 78751, 21090, 78501, 21342, 78251, 21594, 78001, 21846, 77751, 22098, 77501]

c=100000

solveKnapsack(w,v,c)