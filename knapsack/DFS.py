

class node(object):
    def __init__(self, name, weight, value):
        self.name=str(name)
        self.weight=weight
        self.value=value
    def getWeight(self):
        return self.weight
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def __str__(self):
        return self.name + "(" + str(self.weight) + "/" + str(self.value) + ")"

class edge(object):
    def __init__(self, src, dest):
        self.src=src
        self.dest=dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + "->" + str(self.dest)

class weightedEdge(edge):
    def __init__(self, src, dest, weight):
        self.src=src
        self.dest=dest
        self.weight=weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + '->(' \
            +str(self.weight) + ')'  \
            +str(self.dest)

class diagraph(object):
    def __init__(self):
        self.nodes=set([])
        self.edges={}
    def addNode(self, node):

        if node in self.nodes:
            raise ValueError("Duplicate Node")
        else:
            self.nodes.add(node)
            self.edges[node]=[]
    def addEdge(self, edge):
        src=edge.getSource()
        dest=edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError("Node not in graph")
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res =""
        for k in self.edges:
            for d in self.edges[k]:
                res=res+str(k) + '->' + str(d) + '\n'
        return res[:-1]


class DFSWithGenerator(object):
    def __init__(self, start, end, stack=[]):
        self.start=start
        self.end=end
        self.stack=stack
    def start(self):
        self.initPath=[start]
        self.stack.insert(0,initPath)
        while len(self.stack)!=0:
            tmpPath=stack.pop(0)
            self.lastNode=tmpPath[len(tmpPath)-1]
            if self.lastNode.name==end.name:
                return tmpPath
            for shift in shiftDict[[self.lastNode].spot]:
                new=lastNode.transition(shift)
                if notInPath(new, tmpPath):
                    newpath=tmpPath+[new]
                    stack.insert(0,newpath)
        return None






n1=node("1", 2, 3)
n2=node("2", 4, 3)

print sorted([n1,n2], key=lambda node: node.value/float(node.weight))
g=diagraph()

g.addNode(n1)

g.addNode(n2)
g.addEdge(edge(n1, n2))
print str(g)

print n1.value
n1.value=5
print n1.value
print str(g)