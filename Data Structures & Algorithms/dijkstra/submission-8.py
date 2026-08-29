class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        neighbors = defaultdict(list)
        for edge in edges:
            u,v,w = edge
            neighbors[u].append([w,v])
            if v not in neighbors: 
                neighbors[v] = []

        shortest = {}
        heap = [[0,src]]
        while heap:
            node = heapq.heappop(heap)
            distance, edge = node
            if edge in shortest:
                continue
            shortest[edge] = distance

            for weight, edge2 in neighbors[edge]:
                if edge2 in shortest:
                    continue
                heapq.heappush(heap, [distance+weight, edge2])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1        
        return shortest
