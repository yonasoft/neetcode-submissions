class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = Counter(s)
        for char in t:
            if char in s_map:
                s_map[char] -= 1
            else: 
                return False
        for diff in s_map.values():
            if diff != 0:
                return False
        return True
