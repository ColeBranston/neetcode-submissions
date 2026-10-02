class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxx = 0
        l,r = 0, len(heights)-1
        
        while l < r:
            maxx = max(maxx, min(heights[l], heights[r]) * (r-l))

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

        return maxx