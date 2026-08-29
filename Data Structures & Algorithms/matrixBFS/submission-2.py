class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        length = 0
        q = deque([(0,0)])
        visited = set([(0,0)])

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == len(grid)-1 and c == len(grid[0])-1:
                    return length
                neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
                for rd, cd in neighbors:
                    rn, cn = r+rd, c+cd
                    if (rn, cn) in visited:
                        continue
                    if rn == len(grid) or cn == len(grid[0]) or min(rn, cn) < 0:
                        continue
                    if grid[rn][cn] == 1:
                        continue
                    q.append((rn,cn))
                    visited.add((rn,cn))
            length += 1
        return -1 