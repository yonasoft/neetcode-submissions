class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = {}
        l = 0
        res = 0
        for r in range(len(s)):
            curr = s[r]
            if curr in substring and l <= substring[curr]:
                l = substring[curr] + 1
            substring[curr] = r
            res = max(res, r-l+1)
        return res