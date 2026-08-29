from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue  # 跳过未填充的单元格
                
                # 检查行、列和子方格是否已经包含该数字
                if num in rows[r] or num in cols[c] or num in squares[(r//3, c//3)]:
                    return False
                
                # 将数字添加到行、列和子方格的集合中
                rows[r].add(num)
                cols[c].add(num)
                squares[(r//3, c//3)].add(num)
        
        return True