import queue

class Node:
    def __init__(self, val):
        self.val = val
        self.adjList = []
        self.color = False
        self.parent = None

    def insert(self, n):
        self.adjList.append(n)

    def getVal(self):
        return self.val

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def calcAdj(self):
        for e in self.edges:
            st = e.getStart()
            en = e.getEnd()
            st.insert(en)
            en.insert(st)

    def bfs(self, start, end):
        q = queue.Queue()
        start.color = True
        q.put(start)
        while q:
            n = q.get()
            if n is end:
                return n
            for a in n.adjList:
                if not a.color:
                    a.color = True
                    a.parent = n
                    q.put(a)
        return None

def main():
    nodes = [Node(0), Node(1), Node(2), Node(3), Node(4)]
    edges = [Edge(nodes[0], nodes[1]), Edge(nodes[0], nodes[2]), Edge(nodes[2], nodes[1]),
            Edge(nodes[1], nodes[3]), Edge(nodes[0], nodes[4])]

    g = Graph(nodes, edges)
    g.calcAdj()
    ret = g.bfs(nodes[0], nodes[3])
    retArr = []
    while ret:
        retArr.append(ret)
        ret = ret.parent

    for i in range(len(retArr)-1, -1, -1):
        if i == 0:
            print(retArr[i].getVal())
        else:
            print(str(retArr[i].getVal()) + " => ", end='')

main()
