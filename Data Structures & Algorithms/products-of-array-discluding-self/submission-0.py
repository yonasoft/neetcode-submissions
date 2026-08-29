class Solution:
    
    

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = res[i-1] * nums[i-1] if i > 0 else 1
        right_product = 1
        for i in range(len(nums) - 2, -1, -1):
            nums[i] *= nums[i + 1] 
            res[i] *= nums[i + 1] 
        return res
        
        