class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        largest = 0
        for i in range(len(s)):
            sub = set()
            for j in range(i, len(s)):
                if s[j] in sub:
                    break
                sub.add(s[j])
                largest = max(largest, len(sub))
        return largest