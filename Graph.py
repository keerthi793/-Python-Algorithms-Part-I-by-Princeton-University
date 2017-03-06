class Graph:
    def __init__(self):
        self.g = {}

    def addedge(self, v, e):
        if self.g.get(v) is None:
            self.g.update({v: []})
        if self.g.get(e) is None:
            self.g.update({e: []})
        self.g.get(v).append(e)
        self.g.get(e).append(v)
        
    def printvw(self):
        for vertex in range(len(self.g)):
            for edge in self.g.get(vertex):
                print(vertex,'-',edge)


class DFS:
    def __init__(self, g, s):
        self.edgeTo = []
        self.marked = []
        for i in range(0, len(g)):
            self.marked.append(False)
            self.edgeTo.append(None)
            pass
        self.dfs(g, s)

    def dfs(self, g, v):
        self.marked[v] = True
        for j in g.get(v):
            if self.marked[j] == False:
                self.dfs(g, j)
                self.edgeTo[j] = v
        return self.marked
    
    def haspath(self, v):
        return self.marked[v]
    
    def paths(self, s, v):
        if not self.haspath(v):
            return None
        self.path = []
        while v != s:
            x = v
            self.path.append(x)
            v = self.edgeTo[x]
        self.path.append(s)
        return self.path
            
            

G = Graph()
G.addedge(0, 1)
G.addedge(0, 2)
G.addedge(0, 5)
G.addedge(0, 6)
G.addedge(3, 4)
G.addedge(3, 5)
G.addedge(4, 5)
G.addedge(4, 6)
G.addedge(7, 8)
G.addedge(9, 10)
G.addedge(9, 11)
G.addedge(9, 12)
G.addedge(11, 12)
#G.printvw()
d = DFS(G.g, 0)
print(d.paths(0, 6))
#print(G.g)
#print(d.edgeTo)
#print(d.marked)

