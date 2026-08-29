class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        count = 0
        def dfs(row, col, visited):
            if (row, col) in visited or row == len(grid) or col == len(grid[0]) or min(row, col) < 0 or grid[row][col] == 1:
                return 0
            if row == len(grid)-1 and col == len(grid[0])-1:
                return 1
            visited.add((row, col))

            count = 0
            count += dfs(row+1, col, visited)
            count += dfs(row-1, col, visited)
            count += dfs(row, col+1, visited)
            count += dfs(row, col-1, visited)
            visited.remove((row,col))

            return count
        return dfs(0,0,set())
