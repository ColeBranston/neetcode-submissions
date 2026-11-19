class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = prices[0]
        res = float('-inf')

        for r in range(len(prices)):
            if prices[r] < minn:
                minn = prices[r]

            else:
                res = max(res, prices[r] - minn)
        
        return res