class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1,2,3,4]
        # 1 indexed
        # non-equal
        # return pairs that euqal target
        l, r = 0, len(numbers)-1
        while l < r:
            sum_n = numbers[l] + numbers[r]
            if sum_n < target:
                l += 1
            elif sum_n > target:
                r -= 1
            else:
                return [l+1, r+1]
        return [] 