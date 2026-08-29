class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        max_count = 0
        for n in nums:
            if n-1 in unique:
                continue
            curr = n
            while curr in unique:
                curr += 1
            max_count = max(curr-n, max_count)
        return max_count