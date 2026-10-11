class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(rem):
            if rem == 0:
                return 0
            if rem in cache:
                return cache[rem]

            smallest = float('inf')
            for c in coins:
                if rem - c >= 0:
                    smallest = min(smallest, 1 + dfs(rem - c))

            cache[rem] = smallest
            return smallest

        res = dfs(amount)
        return res if res != float('inf') else -1