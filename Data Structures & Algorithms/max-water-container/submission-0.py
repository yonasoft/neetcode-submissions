class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_water = 0
        while l < r:
            width = r - l 
            height = min(heights[l], heights[r])
            max_water = max(max_water, width * height)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_water