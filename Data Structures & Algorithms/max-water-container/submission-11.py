class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ''' 
        normally you find the two maxes and then take the smaller of the two and the distance
        between them which is r-l+1 (window size) and multiply
        '''

        maxx = 0
        l,r = 0,len(heights)-1
        while l < r:
            print(l,r)
            h1 = heights[l]
            h2 = heights[r]
            maxx = max(maxx, (r-l)*min(h1,h2))

            if h2 <= h1:
                r-=1

            else:
                l+=1


        return maxx

