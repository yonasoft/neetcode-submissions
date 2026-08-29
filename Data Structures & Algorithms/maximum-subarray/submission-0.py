class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest, curr = nums[0], 0
        for r in range(len(nums)):
            if curr < 0: 
                curr = 0
            curr += nums[r]
            largest = max(largest, curr)
        return largest

