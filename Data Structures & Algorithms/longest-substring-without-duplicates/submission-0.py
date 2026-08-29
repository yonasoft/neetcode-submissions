class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            curr = s[r]
            while curr in substring:
                substring.remove(s[l])
                l+=1
            substring.add(curr)
            longest = max(longest, len(substring))
        return longest