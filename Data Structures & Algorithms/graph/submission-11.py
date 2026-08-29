class Graph:
    
    def __init__(self):
        self.edges = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        if dst not in self.edges: self.edges[dst] = set()
        self.edges[src].add(dst)
        

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.edges or dst not in self.edges[src]:
            return False
        self.edges[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        return self.dfs(src, dst, set())
        
    def dfs(self, src, dst, visited):
        if src == dst: 
            return True
        visited.add(src)
        for neighbor in self.edges.get(src, []):
            if neighbor not in visited:
                if self.dfs(neighbor, dst, visited): 
                    return True
        return False
