class Graph:
    def __init__(self,V,E):
        self.V = set(V)
        self.E = set(frozenset((u,v)) for u,v in E)
        self._nbrs = {}
        for v in V:
            #self._nbrs[v]=set()
            self.add_vertex(v)
        for u,v in self.E:
            # self._nbrs[u].add(v)
            # self._nbrs[v].add(u)
            self.add_edge(u,v)
    def add_vertex(self,v):
        if v not in self._nbrs:
            self.V.add(v)
        self._nbrs[v]=set
    def add_edge(self,u,v):
        self._nbrs[u].add(v)
        self._nbrs[v].add(u)
    def deg(self,v):
        return sum(1 for e in self.E if v in e)
if __name__=='__main__':
    G = Graph({1,2,3},{(1,2),(2,3)})