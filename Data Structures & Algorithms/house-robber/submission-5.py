class Solution:
    def rob(self, nums: List[int]) -> int:

        '''
        Very similar to climbing stairs, although we instead do the max of i + 2 and i + 3 since we
        cant do adjacent houses, i + 3 covers hypothetically any other house skip funny enough
        '''
        n = len(nums)
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return 0
            if cache[i] != -1:
                return cache[i]

            cache[i] = nums[i] + max(dfs(i+2), dfs(i+3))
            return cache[i]


        return max(dfs(0), dfs(1))