class Graph:
    
    def __init__(self):
        self.edges = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        self.edges[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.edges and dst in self.edges[src]:
            self.edges[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        return self.dfs(src, dst, set())
        
    def dfs(self, src, dst, visited):
        if src == dst:
            return True
        visited.add(src)
        for neighbor in list(self.edges[src]):
            if neighbor in visited:
                continue
            if self.dfs(neighbor, dst, visited):
                return True
        return False

