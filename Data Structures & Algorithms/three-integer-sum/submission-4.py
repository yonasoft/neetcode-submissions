class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0: break
            if i > 0 and n == nums[i-1]: continue 

            l, r = i + 1, len(nums)-1
            while l < r:
                total = n + nums[l] + nums[r]
                if total == 0:
                    res.append([n,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1 
                elif total < 0:
                    l += 1
                else:
                    r-=1
        return res
                

