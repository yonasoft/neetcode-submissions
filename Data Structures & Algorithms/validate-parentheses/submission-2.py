class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        stack  = []
        for c in s:
            if c not in matches:
                stack.append(c)
            else:
                if not stack or stack[-1] != matches[c]:
                    return False
                else:
                    stack.pop()
        return not stack