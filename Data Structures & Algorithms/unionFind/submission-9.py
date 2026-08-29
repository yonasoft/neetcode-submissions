class UnionFind:
    
    def __init__(self, n: int):
        self.parents = {}
        self.rank = {}

        for i in range(n):
            self.parents[i] = i
            self.rank[i] = 1

    def find(self, x: int) -> int:
        curr = self.parents[x]
        while curr != self.parents[curr]:
            self.parents[curr] = self.parents[self.parents[curr]]
            curr = self.parents[curr]
        return curr

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False
        if self.rank[p1] < self.rank[p2]:
            self.parents[p1] = self.parents[p2]
        elif self.rank[p1] > self.rank[p2]:
            self.parents[p2] = self.parents[p1]
        else:
            self.parents[p1] = self.parents[p2]
            self.rank[p2] += 1
        return True

    def getNumComponents(self) -> int:
        roots = set()
        for parent in self.parents.keys():
            roots.add(self.find(parent))
        return len(roots)
