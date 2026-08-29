class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest, curr = nums[0], 0
        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            largest =  max(largest, curr)
        return largest

