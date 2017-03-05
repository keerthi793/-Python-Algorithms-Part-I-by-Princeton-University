from pprint import pprint


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
            if not self.marked[j]:
                self.dfs(g, j)
                self.edgeTo[v] = v

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
d = DFS(G.g, 0)
pprint(G.g)
print(d.edgeTo, d.marked)
# print(len(G.g.get(3)))
