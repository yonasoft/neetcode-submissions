# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrities = []
        for j in range(n):
            knowers = 0
            knows_anybody = False
            for i in range(n):
                if knows(i,j):
                    knowers += 1
                if i != j and knows(j, i):
                    knows_anybody = True
            if knowers == n and not knows_anybody:
                celebrities.append(j)
        return celebrities[0] if len(celebrities) >= 1 else -1