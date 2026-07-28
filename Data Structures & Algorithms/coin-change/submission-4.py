class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(amount):
            if amount == 0:
                return 0

            if amount in cache:
                return cache[amount]

            res = float('inf')
            for coin in coins:
                if amount - coin >= 0: # doens't make calls for coins greater than the amount
                    res = min(res, 1 + dfs(amount-coin)) # on a per-call basis essentially just always keeping the smallest number of coins

            cache[amount] = res
            return res

        minn = dfs(amount)
        return -1 if minn == float('inf') else minn