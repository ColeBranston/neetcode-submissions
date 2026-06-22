class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            O(n^2): just itterate through and set a max variable with the max distance
                 between the current element and any of the following stock prices
                 
        '''

        maxx = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                maxx = max(maxx, prices[j] - prices[i])

        return maxx