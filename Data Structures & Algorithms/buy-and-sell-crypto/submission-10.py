class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            O(n^2): just itterate through and set a max variable with the max distance
                 between the current element and any of the following stock prices
                 
        '''

        # maxx = 0

        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         maxx = max(maxx, prices[j] - prices[i])

        # return maxx

        '''

            O(N): two pointer buy on the left, sell on the right

        '''

        l,r = 0,1
        maxx = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                maxx = max(maxx, prices[r] - prices[l])

            else:
                l=r

            r+=1
            
        return maxx



