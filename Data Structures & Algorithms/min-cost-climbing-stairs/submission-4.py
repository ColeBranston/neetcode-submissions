class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        '''
        the basic approach is essentially, "at each floor the next floor to choose should be the one with
        the small of the two costs", and this recursively builds itself so that at each floor, the optimized
        choice is made and eventually the min cost is returned. This approach then adds some caching and
        we call it a day.
        '''
        n = len(cost)
        cache = [-1] * n

        def dfs(i):
            if i >= n:
                return 0

            if cache[i] != -1:
                return cache[i]

            cache[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return cache[i]

        return min(dfs(0), dfs(1))