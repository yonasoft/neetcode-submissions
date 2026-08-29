class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)
        for n in s:
            if n-1 in s:
                continue
            else:
                length = 1
                while n+length in s:
                    length += 1
                longest = max(longest, length)
        return longest
