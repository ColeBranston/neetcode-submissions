class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxx = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         maxx = max(maxx, prices[j]-prices[i])

        # return maxx
        # Time: O(n^2)
        # Space: O(1)

        l = 0
        maxx = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            print(prices[l], prices[r])
            maxx = max(maxx, prices[r] - prices[l])

        return maxx
        # Time: O(N)
        # Space: O(1)


