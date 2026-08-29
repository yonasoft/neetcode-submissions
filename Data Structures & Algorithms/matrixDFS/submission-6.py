class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        def helper(r,c):
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]):
                return 0
            if grid[r][c] == 1:
                return 0
            if (r,c) in visited:
                return 0
            if r == len(grid)-1 and c == len(grid[0])-1:
                return 1

            visited.add((r,c))
            count = 0 
            count += helper(r+1,c)
            count += helper(r-1,c)
            count += helper(r,c+1)
            count += helper(r,c-1)
            visited.remove((r,c))

            return count

        return helper(0,0)
