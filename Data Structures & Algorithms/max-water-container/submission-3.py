class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ''' 
            O(n^2): Check for every element after the current element checking if the l-r * min(l,r)
                    is a new max
        '''

        maxx = -float('inf')

        print(heights)

        for l in range(len(heights)):
            for r in range(l, len(heights)):
                maxx = max(maxx, abs(l-r) * min(heights[l],heights[r]))

        return maxx