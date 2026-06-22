class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ''' 
            O(n^2): Check for every element after the current element checking if the l-r * min(l,r)
                    is a new max
        '''

        # maxx = -float('inf')

        # for l in range(len(heights)):
        #     for r in range(l, len(heights)):
        #         maxx = max(maxx, abs(l-r) * min(heights[l],heights[r]))

        # return maxx

        '''
         O(n): Use two pointer in a similar way 
        '''

        l,r = 0, len(heights)-1
        total = 0

        while l < r:
            area = (r-l) * min(heights[l], heights[r])

            total = max(total, area)

            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        return total